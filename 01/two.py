#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import sys

def decode(line):
    return line[0], int(line[1:])

password = 0
dial = 50
ops = map(decode, sys.stdin.readlines())
for rot, dist in ops:
    if rot == 'R':
        password += (dial + dist) // 100
        dial = (dial + dist) % 100
    else:
        if 0 == dial:
            password -= 1
        password += (100 - dial + dist) // 100
        dial = (dial - dist) % 100

print(password)
