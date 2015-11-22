from tupro.overload import OverloadEnvironment
import unittest


overload = OverloadEnvironment()

class TestOverload(unittest.TestCase):
    
    def test_basic(self):

    	@overload
    	def to_be_overloaded(a):
    		return a

    	@overload
    	def to_be_overloaded(a, b):
    		return a + b

    	self.assertEqual(to_be_overloaded(0), 0)
    	self.assertEqual(to_be_overloaded(2, 3), 5)

    @overload
    def sum(self, a):
    	return a

    @overload
    def sum(self, a, b):
    	return a + b

    def test_in_class(self):
    	
    	self.assertEqual(self.sum(0), 0)
    	self.assertEqual(self.sum(2, 3), 5)