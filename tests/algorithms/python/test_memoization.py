from unittest import TestCase

from algorithms.python.memoization import memo, fibonacci


class TestMemoization(TestCase):
    def test_fibonacci_caches_values(self):
        fibonacci(3)
        fibonacci(5)
        self.assertEqual(2, memo[3])
        self.assertEqual(3, memo[4])

    def test_fibonacci_uses_cached_values(self):
        """
        Test fibonacci uses an incorrect value for fibonacci(3)
        from memoized cache
        """
        memo[3] = 6
        self.assertEqual(6, fibonacci(3))
