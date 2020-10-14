#!/usr/bin/python3

import os
import subprocess

from contextlib import contextmanager


@contextmanager
def change_directory(directory):
    original = os.path.abspath(os.getcwd())

    os.chdir(directory)
    yield

    os.chdir(original)


def build(directory, tags):
    with change_directory(directory):
        subprocess.run([
            'docker', 'build', '--no-cache', *(f'--tag={tag}' for tag in tags), '.'], check=True)
    
    for tag in tags:
        subprocess.run(['docker', 'push', tag], check=True)


if __name__ == '__main__':
    build('cuda/10.1/python/3.7', [
        'ghcr.io/jonghwanhyeon/cuda:python3.7', 'jonghwanhyeon/cuda:python3.7'])
    build('cuda/10.1/python/3.8', [
        'ghcr.io/jonghwanhyeon/cuda:python3.8', 'jonghwanhyeon/cuda:python3.8'])
    build('cuda/10.1/python/3.9', [
        'ghcr.io/jonghwanhyeon/cuda:python3.9', 'jonghwanhyeon/cuda:python3.9', 
        'ghcr.io/jonghwanhyeon/cuda:python3', 'jonghwanhyeon/cuda:python3'])
    
    build('ml/', ['ghcr.io/jonghwanhyeon/ml', 'jonghwanhyeon/ml'])
    build('jupyter/', ['ghcr.io/jonghwanhyeon/jupyter', 'jonghwanhyeon/jupyter'])
    build('jupyterlab/', ['ghcr.io/jonghwanhyeon/jupyterlab', 'jonghwanhyeon/jupyterlab'])
    build('code-server/', ['ghcr.io/jonghwanhyeon/code-server', 'jonghwanhyeon/code-server'])
