# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 should be equilateral')
    
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(7,8,9),'Scalene','7,8,9 should be Scalene')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 should be Scalene')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5,5,7),'Isoceles','5,5,7 should be Isosceles')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(7,7,11),'Isoceles','7,7,11 should be Isosceles')

    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle('g', 4, 6),'InvalidInput','g, 4, 6 should be InvalidInput')

    def testLengthLimit(self): 
        self.assertEqual(classifyTriangle(100, 9, 400),'InvalidInput','100, 9, 400 should be InvalidInput')

    def testNegetiveInput(self): 
        self.assertEqual(classifyTriangle(-5,6,-2),'InvalidInput','-5,6, -2 should be InvalidInput')

    def testForNotATriangle(self): 
        self.assertEqual(classifyTriangle(12,20,5),'NotATriangle','12,14,5 should be NotATriangle')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

