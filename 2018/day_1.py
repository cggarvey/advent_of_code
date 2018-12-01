"""
Solution for https://adventofcode.com/2018/day/1
"""

import os
from collections import deque


def get_data() -> list:

    this_dir = os.path.dirname(__file__)
    data_path = os.path.join(this_dir, "data", "day_1.txt")

    with open(data_path, "r") as fh:
        lines = [int(l.strip()) for l in fh.readlines()]

    return lines


def frequency_generator(changes, seed=0):
    curr_freq = seed
    for delta in changes:
        curr_freq += delta

        yield curr_freq


def part_one(changes: list) -> int:

    dq = deque(frequency_generator(changes), maxlen=1)
    last = dq.pop()

    return last


def part_two(changes: list, prev_freqs: set=None, seed: int=0) -> int:

    if not prev_freqs:
        prev_freqs = set()

    curr_freq = 0

    for curr_freq in frequency_generator(changes, seed):
        if curr_freq in prev_freqs:
            return curr_freq

        prev_freqs.add(curr_freq)

    return part_two(changes, prev_freqs, curr_freq)


if __name__ == '__main__':

    change_list = get_data()

    one = part_one(change_list)
    two = part_two(change_list)

    print("part one answer:", one)
    print("part two answer:", two)
