#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

def decode_range(in_str):
    in_begin, in_end = in_str.split("-")
    return int(in_begin), int(in_end)

ranges = map(decode_range, input().split(","))

sum_invalid_ids = 0

for begin, end in ranges:
    # Ranges seem to be inclusive based on the description of end as
    # "last ID" in the task description.
    for n in range(begin, end + 1):
        word = str(n)
        if len(word) % 2 == 0:
            midpoint = len(word) // 2
            if word[:midpoint] == word[midpoint:]:
                sum_invalid_ids += n

print(sum_invalid_ids)
