#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import sys

grid = [str.rstrip(line) for line in sys.stdin.readlines()]

def in_bounds(x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def is_accessible(x, y):
    offsets = [(1, 0), (-1, 0), (1, 1), (0, 1),
               (-1, 1), (1, -1), (0, -1), (-1, -1)]
    neighbors = [grid[y + dy][x + dx]
                 for dx, dy in offsets
                 if in_bounds(y + dy, x + dx)]
    return neighbors.count('@') < 4

accessible_rolls = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '@' and is_accessible(x, y):
            accessible_rolls += 1

print(accessible_rolls)
