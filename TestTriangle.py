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
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
    
    def testIvalidInput1(self):                                  #Test a or b or c can't >200
        self.assertEqual(classifyTriangle(300,320,330),'InvalidInput') 
    
    def testIvalidInput2(self):                                 #Test a or b or c  can't <= 0
        self.assertEqual(classifyTriangle(-3,7,0), 'InvalidInput') 
    
    def testInvalidInput3(self):                        #Test three inputs must be integers
        self.assertNotEqual(classifyTriangle(4.5,10.5,8.5), 'InvalidInput')

    def tesInvalidInput4(self):
        self.assertEqual(classifyTriangle(4,None,11), 'InvalidInput')
    
    def testNotATriangle1(self):                     #Test the sum of two sides of a triabgle must greater than the third side
        self.assertEqual(classifyTriangle(1,2,4),'NotATriangle')

    def testNotATriangle2(self):                     
        self.assertEqual(classifyTriangle(1,4,2),'NotATriangle')
    
    def testNotATriangle3(self):                     
        self.assertEqual(classifyTriangle(2,4,1),'NotATriangle')

    def testScaleneTriangle1(self):               
        self.assertEqual(classifyTriangle(6,4,9),'Scalene')

    def testScaleneTriangle2(self):               
        self.assertEqual(classifyTriangle(4,3,2),'Scalene')

    def testScaleneTriangle3(self):               
        self.assertEqual(classifyTriangle(2,3,4),'Scalene')    
        
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(1,1,2),'Isosceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(2,1,1),'Isosceles')  

    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(1,1,2),'Isosceles')  
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

