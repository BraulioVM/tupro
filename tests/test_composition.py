import unittest
from tupro.composition import Composable


class TestComposability(unittest.TestCase):
    def test_basic(self):
        @Composable
        def add1(x):
            return x + 1

        def multiply_by_3(x):
            return 3 * x

        collatz_up = add1 * multiply_by_3

        self.assertEqual(collatz_up(10), 31)
        self.assertEqual(collatz_up(25), 76)

    def test_right_mult(self):
        def add1(s):
            return s + "hello"

        @Composable
        def remove_last_chars(s, n):
            return s[:-n]

        method = add1 * remove_last_chars

        self.assertEqual(method("sharar", 3), "shahello")


        
