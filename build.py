#!/usr/bin/python3

import json
import os
import subprocess
import sys

from contextlib import contextmanager


@contextmanager
def change_directory(directory):
    original = os.path.abspath(os.getcwd())

    os.chdir(directory)
    yield
    os.chdir(original)


def build(directory, arguments, tags, options):
    with change_directory(directory):
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
        build(item['dockerfile'], item.get('arguments', {}), item['tags'], build_options)
