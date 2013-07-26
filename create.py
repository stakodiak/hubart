#!/usr/bin/python
from datetime import datetime, timedelta, tzinfo
import subprocess
import shlex
import sys
import time
import os

# From Python's docs:
# https://docs.python.org/2/library/datetime.html
class Eastern(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=4) + self.dst(dt)
    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime(dt.year, 4, 1)   # ends last Sunday in October
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)
    def tzname(self,dt):
         return "Eastern"

def create_commit(dt):
    # Set commit's author date and commit date with
    # environment variables.
    env = os.environ
    if dt.dst():
        dt = dt - timedelta(days=1)
    date = dt.strftime('%a %b %d %T %Y %z')
    for key in ('GIT_AUTHOR_DATE', 'GIT_COMMITTER_DATE'):
        env[key] = date
    print date, bool(dt.dst())
    # Update file and commit it.
    with open('data', 'a') as f:
        f.write('sticks\n')
    command = 'git commit data -m "fish"'
    args = shlex.split(command)
    subprocess.Popen(args, env=env)
    time.sleep(1)

def main():
    # Make sure datetimes have a timezone so we can
    # change for DST.
    start = datetime(2013, 07, 14, tzinfo=Eastern())
    # Create a commit for each td passed to script.
    for td in map(int, sys.argv[1:]):
        date = start + timedelta(days=td)
        create_commit(date)


if __name__ == '__main__':
    main()
