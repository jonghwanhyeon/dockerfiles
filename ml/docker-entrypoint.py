#!/usr/bin/env python3
import subprocess
import os
import sys
import pwd

default_shell = '/bin/bash'

arguments = sys.argv[1:]
if not arguments:
    arguments = [default_shell]
executable = arguments[0]

current_uid = os.getuid()
run_as_user = current_uid != 0

if run_as_user:
    completed = subprocess.run(['docker-init-user'])
    if completed.returncode != 0:
        print("Failed to initialize a user", file=sys.stderr)
        sys.exit(1)

    home_directory = pwd.getpwuid(current_uid).pw_dir
    os.environ['HOME'] = home_directory
    os.chdir(home_directory)

os.execvp(executable, arguments)