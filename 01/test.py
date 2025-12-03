#!/usr/bin/env python3

import sys

def decode(line):
    return line[0], int(line[1:])

password = 0
dial = 50
ops = map(decode, sys.stdin.readlines())
for rot, dist in ops:
    for _ in range(dist):
        if rot == 'R':
            dial = (dial + 1) % 100
        else:
            dial = (dial - 1) % 100

        if 0 == dial:
            password += 1

print(password)
