"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """testing the max int function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([-2, 0, 19, 14]), 19)
        self.assertEqual(max_integer([-10, 10]), 10)
    
    def testNone(self):
        self.assertIsNone(max_integer([]))

    def testType(self):
        self.assertRaises(TypeError, max_integer("a"))

if __name__ == '__main__':
    unittest.main()
