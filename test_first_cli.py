#!/usr/bin/env python3
#New file created


import unittest
import first_cli

#tests for my first command line interface


class TestFirstCli(unittest.TestCase):
    def test_mult(self):
        self.assertEqual(first_cli.mult(2,8), 16) # should be 16
    
    def test_add(self):
        self.assertEqual(first_cli.add(2, 8), 10)

    def test_subtract(self):
        self.assertEqual(first_cli.subtract(8, 2), 6)


    def test_divide(self):
        self.assertEqual(first_cli.divide(8, 2), 4)

    def test_square(self):
        self.assertEqual(first_cli.square(8), 64)

    




if __name__ == '__main__':
    unittest.main()