#!/usr/bin/python3
"unit test for Base class"


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
