#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import sys

ranges = []

while (range_input := sys.stdin.readline().rstrip()):
    start, end = range_input.split("-")
    ranges.append((int(start), int(end)))

fresh_counter = 0
while (query_input := sys.stdin.readline()):
    query = int(query_input)
    if any(start <= query <= end for start, end in ranges):
        fresh_counter += 1

print(fresh_counter)
