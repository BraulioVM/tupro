from tupro import typecheck
import unittest


class TestTypeCheck(unittest.TestCase):
    
    def test_one_parameter(self):

        @typecheck
        def identity(a: int) -> int:
            return a
    
        self.assertEqual(identity(3), 3) # no problems

        with self.assertRaises(TypeError):
            identity("error")


    def test_return_type(self):

        @typecheck
        def almost_identity(a) -> int:
            return a


        self.assertEqual(almost_identity(3), 3)

        with self.assertRaises(TypeError):
            almost_identity("error") # it returns a string, should not