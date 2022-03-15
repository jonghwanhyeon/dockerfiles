#!/usr/bin/python3

import json
import os
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List


@contextmanager
def change_directory(path: Path):
    original = Path.cwd().resolve()

    os.chdir(path)
    yield
    os.chdir(original)


def build(path: Path, arguments: Dict[str, str], tags: List[str], options: List[str]):
    with change_directory(path):
        command = ['docker', 'build']
        command += options

        for key, value in arguments.items():
            command.append('--build-arg')
            command.append(f'{key}={value}')

        command += [f'--tag={tag}' for tag in tags]
        command += ['.']

        subprocess.run(command, check=True)

    for tag in tags:
        subprocess.run(['docker', 'push', tag], check=True)


if __name__ == '__main__':
    build_options = sys.argv[1:]

    with open('config.json', 'r', encoding='utf-8') as input_file:
        config = json.load(input_file)

    for item in config['builds']:
        build(path=Path(item['dockerfile']),
              arguments=item.get('arguments', {}),
              tags=item['tags'],
              options=build_options)
