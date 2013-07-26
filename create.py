#!/usr/bin/python
from datetime import datetime, timedelta
import subprocess
import shlex
import sys
import time
import os

def create_commit(dt):
    # Set commit's author date and commit date with
    # environment variables.
    env = os.environ
    date = dt.strftime('%a %b %d %T %Y -400')
    for key in ('GIT_AUTHOR_DATE', 'GIT_COMMITTER_DATE'):
        env[key] = date
    print date
    # Update file and commit it.
    with open('data', 'a') as f:
        f.write('sticks\n')
    command = 'git commit data -m "fish"'
    args = shlex.split(command)
    subprocess.Popen(args, env=env)
    time.sleep(2)

if __name__ == '__main__':
    main()

def main():
    # Create a commit for each td passed to script.
    start = datetime(2013, 07, 14)
    start += timedelta(hours=12)  # for DST
    for td in map(int, sys.argv[1:]):
        date = start + timedelta(days=td)
        create_commit(date)
