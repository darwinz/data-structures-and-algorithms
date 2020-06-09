import copy
from unittest import TestCase

from algorithms.python.count_the_paths_matrix import count_the_paths, count_the_paths_with_memoization


class TestCountThePaths(TestCase):
    def test_count_the_paths(self):
        # matrix = [
        #     [1, 1, 1, 1, 1, 1, 1, 1],
        #     [1, 1, 0, 1, 1, 1, 0, 1],
        #     [1, 1, 1, 1, 0, 1, 0, 1],
        #     [0, 1, 0, 1, 1, 0, 1, 1],
        #     [1, 1, 0, 0, 1, 1, 0, 1],
        #     [1, 0, 1, 1, 0, 1, 1, 1],
        #     [1, 1, 1, 1, 0, 0, 1, 1],
        #     [1, 1, 1, 1, 1, 1, 1, 1]
        # ]
        matrix = [
            [1, 1],
            [1, 1]
        ]
        # paths = {}
        subject = count_the_paths(matrix, 0, 0, 0)
        self.assertEqual(2, subject)

    def test_count_the_paths_with_memoization(self):
        matrix = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        paths = [[None] * len(matrix[0])] * len(matrix)
        subject = count_the_paths_with_memoization(matrix, 0, 0, paths)
        self.assertEqual(2, subject)
