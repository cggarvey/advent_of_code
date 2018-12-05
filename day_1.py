"""
Solution for https://adventofcode.com/2018/day/1
"""

from utils import io, misc
from collections import deque


def part_one(changes: list) -> int:

    dq = deque(misc.frequency_generator(changes), maxlen=1)
    last = dq.pop()

    return last


def part_two(changes: list, prev_freqs: set=None, seed: int=0) -> int:

    if not prev_freqs:
        prev_freqs = set()

    curr_freq = 0

    for curr_freq in misc.frequency_generator(changes, seed):
        if curr_freq in prev_freqs:
            return curr_freq

        prev_freqs.add(curr_freq)

    return part_two(changes, prev_freqs, curr_freq)


if __name__ == '__main__':

    change_list = io.get_data("day_1.txt", type_conv=int)

    one = part_one(change_list)
    two = part_two(change_list)

    print("part one answer:", one)
    print("part two answer:", two)
