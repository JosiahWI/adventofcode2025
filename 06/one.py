#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import math
import sys

input_matrix = [line.rstrip().split() for line in sys.stdin.readlines()]
problems = zip(*(input_matrix[::-1]))

grand_total = 0
for op, *operands in problems:
    if "+" == op:
        grand_total += sum(int(n) for n in operands)
    else:
        grand_total += math.prod(int(n) for n in operands)

print(grand_total)
