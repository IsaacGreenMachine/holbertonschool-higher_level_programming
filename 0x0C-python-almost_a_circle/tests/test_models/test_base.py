#!/usr/bin/python3
"unit test for Base class"


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(2, 2)


'''
Working Cases:

Error Cases:
init(None)
init(-4)
init("ha")
init(2, 3)
init, init (id should be 2?)
init(4), init() (id should be 1?)
to_json_string({})
to_json_string(4)
to_json_string([{},{},{}])
to_json_string({"this": "that"})


'''


if __name__ == '__main__':
    unittest.main()
