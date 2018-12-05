"""
Solution for https://adventofcode.com/2018/day/2
"""

from utils import io, misc
from itertools import combinations


def part_one(boxes):
    contains_two = 0
    contains_three = 0

    for box in boxes:

        letter_cts = misc.letter_counts(box)
        count_values = letter_cts.values()

        if 2 in count_values:
            contains_two += 1

        if 3 in count_values:
            contains_three += 1

    return contains_two * contains_three


def part_two(boxes) -> tuple:

    combos = combinations(boxes, 2)

    best_pair = None
    best_score = 0
    best_wc = None

    for a, b in combos:

        wc = wildcardize(a, b)
        score = len(wc) - wc.count("*")

        if score > best_score:
            best_pair = (a, b)
            best_score = score
            best_wc = wc

    return best_pair, best_score, best_wc


def wildcardize(string_a, string_b) -> str:

    output = ""

    for l_a, l_b in zip(string_a, string_b):
        if l_a == l_b:
            output += l_a
        else:
            output += "*"

    return output


def test_part_one():

    boxes = io.get_data("test_day_2_part_one.txt", type_conv=str)
    actual = part_one(boxes)

    assert actual == 12


def test_part_two():

    boxes = io.get_data("test_day_2_part_two.txt", type_conv=str)

    best_pair, best_score, wc = part_two(boxes)

    assert wc.replace("*", "") == "fgij"
    assert best_score == 4


def test():

    test_part_one()
    test_part_two()


def main():
    box_ids = io.get_data("day_2.txt", type_conv=str)

    # part one of the exercise
    checksum = part_one(box_ids)
    print(f"Checksum: {checksum}")

    pair, score, wc = part_two(box_ids)
    print(f"Best Pair: {pair}")
    print(f"{score} letters in common:", wc.replace("*", ""))


if __name__ == '__main__':
    main()
    test()
