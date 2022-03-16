#!/usr/bin/python3

import json
import subprocess
import sys
import time
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List


def retry(number_of_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, number_of_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exception:
                    if attempt >= number_of_attempts:
                        raise exception

                    print('An error occurred:', exception)
                    print('Retry after 15 seconds...')
                    time.sleep(15)

        return wrapper
    return decorator

@retry(number_of_attempts=3)
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

@retry(number_of_attempts=3)
def push(tags: List[str]):
    for tag in tags:
        subprocess.run(['docker', 'push', tag], check=True, timeout=600)


if __name__ == '__main__':
    build_options = sys.argv[1:]

    with open('config.json', 'r', encoding='utf-8') as input_file:
        config = json.load(input_file)

    for item in config['builds']:
        build(dockerfile_path=Path(item['dockerfile']),
              arguments=item.get('arguments', {}),
              tags=item['tags'],
              options=build_options)
        push(tags=item['tags'])

    tags_by_dockerfile = OrderedDict()
    for item in config['builds']:
        tags_by_dockerfile.setdefault(item['dockerfile'], []).extend(item['tags'])

    with open('README.md', 'w', encoding='utf-8') as output_file:
        print('# Dockerfiles', file=output_file)

        for dockerfile, tags in tags_by_dockerfile.items():
            print(f'## {dockerfile}', file=output_file)
            for tag in tags:
                print(f'- `{tag}`', file=output_file)
            print(file=output_file)
