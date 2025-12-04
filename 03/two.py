#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import sys

banks = map(str.rstrip, sys.stdin.readlines())

# This solution is based on the understanding that we always need
# to turn on 12 batteries per bank and a battery with joltage A will
# contribute up to 9 jolts in the least significant digit position, but
# no less than 10 jolts in the second least significant digit position.
#
# From these considerations we derive a greedy approach that assigns
# the highest value battery to the next significant digit's place,
# working from most to least significant and reserving enough space at
# the end of the bank for the remaining batteries. If there is more
# than one battery that could satisfy the requirement, we choose the
# leftmost one in the bank so that the solution can use other high
# value batteries in the rest of the bank.

def get_max_joltage(bank_subseq, batteries_needed, joltage_so_far):e
    if 0 == batteries_needed:
        return joltage_so_far

    index_of_maximum = -1
    current_maximum = -1
    # Reserve the minimum space at the end of the bank for finding
    # the remaining batteries.
    for i in range(len(bank_subseq) - (batteries_needed - 1)):
        n = bank_subseq[i]
        # It is important that we keep the maximum with the lowest index
        # if there are multiple, hence use strictly greater.
        if n > current_maximum:
            current_maximum = n
            index_of_maximum = i

    digit = bank_subseq[index_of_maximum]

    return get_max_joltage(bank_subseq[index_of_maximum + 1:],
                       batteries_needed - 1,
                       joltage_so_far * 10 + digit)
    

sum_max_joltages = 0
for bank in map(lambda b: [int(d) for d in b], banks):
    sum_max_joltages += get_max_joltage(bank, 12, 0)

print(sum_max_joltages)
