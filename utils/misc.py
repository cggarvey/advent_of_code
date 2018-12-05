from collections import defaultdict


def frequency_generator(changes, seed=0):
    curr_freq = seed
    for delta in changes:
        curr_freq += delta

        yield curr_freq


def letter_counts(string: str) -> dict:
    d = defaultdict(int)

    for ltr in string:
        d[ltr] += 1

    return d
