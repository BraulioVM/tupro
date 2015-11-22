import unittest
from tupro import defaultify


class TestDefaultify(unittest.TestCase):
    def test_basic(self):
        def wrong_typical_method(a = []):
            a.append("a")
            return a == ["a"]

        @defaultify
        def defaultified_method(a = []):
           a.append("a")
           return a == ["a"]


        self.assertTrue(wrong_typical_method())
        self.assertFalse(wrong_typical_method())

        self.assertTrue(defaultified_method())
        self.assertTrue(defaultified_method()) # works
        
    def test_multiple_parameter_list(self):
        @defaultify
        def k(a = [], b = []):
            a.append("hola")
            b.append("hey")

            return len(a) == 1 == len(b)


        k() # true

        self.assertTrue(k())
