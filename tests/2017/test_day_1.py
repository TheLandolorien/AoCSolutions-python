from unittest import TestCase
from importlib import import_module

ENV = 'Testing'
YEAR = 2017
ADVENT = 12
DAY = 1


class Test2017Day1(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.puzzle_solution = import_module('app.solutions.{}.day_{}'.format(YEAR, DAY))


class Part1(Test2017Day1):
    def test_part_1_solution_sample_input_1(self):
        sample_input = '1122'
        expected_solution = 3

        actual_solution = self.puzzle_solution.part_1(sample_input)
        self.assertEqual(expected_solution, actual_solution,
                         'Day 2, Part 1 - 2017 failed for input: {}'.format(sample_input))

    def test_part_1_solution_sample_input_2(self):
        sample_input = '1111'
        expected_solution = 4

        actual_solution = self.puzzle_solution.part_1(sample_input)
        self.assertEqual(expected_solution, actual_solution,
                         'Day 2, Part 1 - 2017 failed for input: {}'.format(sample_input))

    def test_part_1_solution_sample_input_3(self):
        sample_input = '1234'
        expected_solution = 0

        actual_solution = self.puzzle_solution.part_1(sample_input)
        self.assertEqual(expected_solution, actual_solution,
                         'Day 2, Part 1 - 2017 failed for input: {}'.format(sample_input))

    def test_part_1_solution_sample_input_4(self):
        sample_input = '91212129'
        expected_solution = 9

        actual_solution = self.puzzle_solution.part_1(sample_input)
        self.assertEqual(expected_solution, actual_solution,
                         'Day 2, Part 1 - 2017 failed for input: {}'.format(sample_input))


class Part2(Test2017Day1):
    def test_part_2_solution_sample_input_1(self):
        sample_input = '1212'
        expected_solution = 6

        actual_solution = self.puzzle_solution.part_2(sample_input)
        self.assertEqual(expected_solution, actual_solution,
                         'Day 2, Part 2 - 2017 failed for input: {}'.format(sample_input))

    def test_part_2_solution_sample_input_2(self):
        sample_input = '1221'
        expected_solution = 0

        actual_solution = self.puzzle_solution.part_2(sample_input)
        self.assertEqual(expected_solution, actual_solution,
                         'Day 2, Part 2 - 2017 failed for input: {}'.format(sample_input))

    def test_part_2_solution_sample_input_3(self):
        sample_input = '123123'
        expected_solution = 12

        actual_solution = self.puzzle_solution.part_2(sample_input)
        self.assertEqual(expected_solution, actual_solution,
                         'Day 2, Part 2 - 2017 failed for input: {}'.format(sample_input))

    def test_part_2_solution_sample_input_4(self):
        sample_input = '12131415'
        expected_solution = 4

        actual_solution = self.puzzle_solution.part_2(sample_input)
        self.assertEqual(expected_solution, actual_solution,
                         'Day 2, Part 2 - 2017 failed for input: {}'.format(sample_input))
