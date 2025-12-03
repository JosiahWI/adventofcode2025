#!/usr/bin/env python3

# Copyright (C) Josiah VanderZee 2025

import itertools

def decode_range(in_str):
    in_begin, in_end = in_str.split("-")
    return int(in_begin), int(in_end)

ranges = map(decode_range, input().split(","))

sum_invalid_ids = 0

def all_same(iterable):
    l = list(iterable)
    return l and all(s == l[0] for s in l)

def repeats_every(x, word):
    chunk_size, chunk_mod = divmod(len(word), x)
    return chunk_mod == 0 and \
            len(word) > chunk_size and \
            all_same(itertools.batched(word, chunk_size))

for begin, end in ranges:
    # Ranges seem to be inclusive based on the description of end as
    # "last ID" in the task description.
    for n in range(begin, end + 1):
        word = str(n)
        for prime in [2, 3, 5, 7]:
            if repeats_every(prime, word):
                sum_invalid_ids += n
                break

print(sum_invalid_ids)
