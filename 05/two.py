#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import sys

ranges = []

while (range_input := sys.stdin.readline().rstrip()):
    start, end = range_input.split("-")
    ranges.append((int(start), int(end)))

ranges.sort()

fresh_ids = 0

while len(ranges) > 1:
    start1, end1 = ranges.pop(0)
    start2, end2 = ranges[0]
    if end1 < start2:
        fresh_ids += (end1 - start1 + 1)
    elif end1 >= start2:
        if start1 <= start2:
            if end1 >= end2:
                ranges[0] = (start1, end1)
            else:
                fresh_ids += (start2 - start1)
        else:
            assert(end2 >= end1)

start, end = ranges[-1]
fresh_ids += (end - start + 1)

print(fresh_ids)
