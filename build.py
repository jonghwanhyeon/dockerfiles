#!/usr/bin/python3

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List


def build(dockerfile_path: Path,
          arguments: Dict[str, str],
          tags: List[str],
          options: List[str]):
    command = ['docker', 'build']
    command.append(f'--file={dockerfile_path}')
    command.extend(options)

    for key, value in arguments.items():
        command.append('--build-arg')
        command.append(f'{key}={value}')

    command.extend([f'--tag={tag}' for tag in tags])
    command.append(str(dockerfile_path.parent.resolve()))

    subprocess.run(command, check=True)

    for tag in tags:
        subprocess.run(['docker', 'push', tag], check=True)


if __name__ == '__main__':
    build_options = sys.argv[1:]

    with open('config.json', 'r', encoding='utf-8') as input_file:
        config = json.load(input_file)

    for item in config['builds']:
        build(dockerfile_path=Path(item['dockerfile']),
              arguments=item.get('arguments', {}),
              tags=item['tags'],
              options=build_options)
