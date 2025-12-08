#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import itertools
import math
import sys

input_matrix = [line.rstrip() for line in sys.stdin.readlines()]
operators = input_matrix[-1].split()

transpose = itertools.zip_longest(*(input_matrix[:-1]), fillvalue=" ")
problem_lines = map("".join, transpose)
problems = map(lambda t: t[1], filter(lambda t: t[0],
                  itertools.groupby(problem_lines, lambda line: not line.isspace())))

grand_total = 0
for op, operands in zip(operators, problems):
    if "+" == op:
        grand_total += sum(int(n) for n in operands)
    else:
        grand_total += math.prod(int(n) for n in operands)

print(grand_total)
