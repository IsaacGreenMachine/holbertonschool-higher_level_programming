#!/usr/bin/python3
"unit test for Base class"


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(2, 2)


'''
init(3, 5, 9, 1, 4)
init(-3, 1)
init(2, -4)
init(-0, -0)
init(0, 0)
init(2, 0)
init(0, 2)
init("hello")
init(2, "that")
'''

if __name__ == '__main__':
    unittest.main()
