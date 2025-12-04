#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import sys

banks = map(str.rstrip, sys.stdin.readlines())

sum_max_joltages = 0
for bank in map(lambda b: [int(d) for d in b], banks):
    index_of_maximum = -1
    current_maximum = -1
    # We don't include the last element in this search for the first digit,
    # because the last element has no element after it to be the second digit.
    for i in range(len(bank) - 1):
        n = bank[i]
        # It is important that we keep the maximum with the lowest index
        # if there are multiple, hence use strictly greater.
        if n > current_maximum:
            current_maximum = n
            index_of_maximum = i

    first_digit = bank[index_of_maximum]
    second_digit = max(bank[index_of_maximum + 1:])

    sum_max_joltages += (first_digit * 10 + second_digit)

print(sum_max_joltages)
