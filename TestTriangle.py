# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class testTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_right_triangle_a(self):
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_equilateral_triangle_a(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_equilateral_triangle_b(self):
        self.assertEqual(classify_triangle(5,5,5),'Equilateral','5,5,5 should be equilateral')

    def test_scalene_triangle_a(self):
        self.assertEqual(classify_triangle(7,8,9),'Scalene','7,8,9 should be Scalene')

    def test_scalene_triangle_b(self):
        self.assertEqual(classify_triangle(5,6,7),'Scalene','5,6,7 should be Scalene')

    def test_isosceles_triangle_a(self):
        self.assertEqual(classify_triangle(5,5,7),'Isoceles','5,5,7 should be Isosceles')

    def test_isosceles_triangle_b(self):
        self.assertEqual(classify_triangle(7,7,11),'Isoceles','7,7,11 should be Isosceles')

    def test_invalid_input(self):
        self.assertEqual(classify_triangle('g', 4, 6),'InvalidInput','g, 4, 6 should be InvalidInput')

    def test_length_limit(self):
        self.assertEqual(classify_triangle(100, 9, 400),'InvalidInput','100, 9, 400 should be InvalidInput')

    def test_negetive_input(self):
        self.assertEqual(classify_triangle(-5,6,-2),'InvalidInput','-5,6, -2 should be InvalidInput')

    def test_for_not_a_triangle(self):
        self.assertEqual(classify_triangle(12,20,5),'NotATriangle','12,14,5 should be NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
