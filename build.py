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


def build(directory, tags, options):
    with change_directory(directory):
        subprocess.run([
            'docker', 'build', 
                *options,
                *[f'--tag={tag}' for tag in tags], 
                '.'], check=True)

    for tag in tags:
        subprocess.run(['docker', 'push', tag], check=True)


if __name__ == '__main__':
    build_options = sys.argv[1:]

    with open('config.json', 'r', encoding='utf-8') as input_file:
        config = json.load(input_file)
    
    for item in config['builds']:
        build(item['dockerfile'], item['tags'], build_options)
