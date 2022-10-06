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
    
    def test_negative_numbers(self):
        self.assertEqual(first_cli.add(-2, 8), 6)


    def test_subtract(self):
        self.assertEqual(first_cli.subtract(8, 2), 6)

    def test_subtract_negatives(self):
        self.assertEqual(first_cli.subtract(-2, -2), 0)


    def test_divide(self):
        self.assertEqual(first_cli.divide(8, 2), 4)

    def test_square(self):
        self.assertEqual(first_cli.square(8), 64)

    def test_sub_polynomial(self):
        self.assertEqual(first_cli.sub_polynomial(4,4), 0)

    def test_add_polynomial(self):
        self.assertEqual(first_cli.add_polynomial(3, 3), 18)
        
    def test_threevariables(self):
        self.assertEqual(first_cli.threeVar(2, 2, 2), 36)
    
    def test_cube_root(self):
        self.assertEqual(first_cli.cube_root(2), 8)

    def test_create_exponent(self):
        self.assertEqual(first_cli.create_exponent(10, 2), 100)





if __name__ == '__main__':
    unittest.main()