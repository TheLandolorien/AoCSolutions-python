"""Advent of Code Solution

Create solutions for daily puzzles.

Flask route expects at least a part_1 and part_2 method.
Additional methods can be added as needed.
Puzzle Input will be sent as 'input' parameter.

"""


def part_1(puzzle_input):
    """ Day 1: Inverse Captcha - Part 1
    The captcha requires you to review a sequence of digits (your puzzle input) and
    find the sum of all digits that match the next digit in the list. The list is
    circular, so the digit after the last digit is the first digit in the list.
    """
    shift = 1
    return captcha(shift, puzzle_input)


def part_2(puzzle_input):
    """ Day 1: Inverse Captcha - Part 2
    Now, instead of considering the next digit, it wants you to consider the digit
    halfway around the circular list. That is, if your list contains 10 items, only
    include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
    Fortunately, your list has an even number of elements.
    """

    shift = len(puzzle_input) / 2
    return captcha(shift, puzzle_input)


def captcha(n, captcha):
    size = len(captcha)
    return sum([int(num) for i, num in enumerate(captcha) if num == captcha[int((i + n) % size)]])
