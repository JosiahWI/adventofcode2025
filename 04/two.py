#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import sys

grid = [list(str.rstrip(line)) for line in sys.stdin.readlines()]

def in_bounds(x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def is_accessible(x, y):
    offsets = [(1, 0), (-1, 0), (1, 1), (0, 1),
               (-1, 1), (1, -1), (0, -1), (-1, -1)]
    neighbors = [grid[y + dy][x + dx]
                 for dx, dy in offsets
                 if in_bounds(y + dy, x + dx)]
    return neighbors.count('@') < 4

total_rolls_moved = 0
while True:
    accessible_rolls = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@' and is_accessible(x, y):
                accessible_rolls += 1
                # It is safe to remove the roll during this pass, because any
                # effect it has on the rest of the pass is the same effect it
                # would otherwise have on the next pass.
                grid[y][x] = 'x'

    # We may or may not have removed every single roll when this happns.
    if 0 == accessible_rolls:
        break
    total_rolls_moved += accessible_rolls

print(total_rolls_moved)
