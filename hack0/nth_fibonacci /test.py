import unittest
import solution


class NthFibonacciTest(unittest.TestCase):
    """docstring for NthFibonacciTest"""
    def test_nth_fibonacci(self):
        self.assertEqual(2, solution.nth_fibonacci(3))
        self.assertEqual(55, solution.nth_fibonacci(10))

if __name__ == '__main__':
    unittest.main()