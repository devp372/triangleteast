# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a_side,b_side,c_side):
    res = ""

    if not(isinstance(a_side,int) and isinstance(b_side,int) and isinstance(c_side,int)):
        res = 'InvalidInput'
    elif a_side >= 200 or b_side >= 200 or c_side >= 200:
        res = 'InvalidInput'
    elif a_side <= 0 or b_side <= 0 or c_side <= 0:
        res = 'InvalidInput'
    elif (a_side > (b_side + c_side)) or (b_side > (a_side + c_side)) or (c_side > (a_side + b_side)):
        res = 'NotATriangle'
    elif a_side == b_side and b_side == c_side:
        res = 'Equilateral'
    elif ((a_side**2 + b_side**2) == c_side**2) or ((a_side**2 + c_side**2) == b_side**2) or ((b_side**2 + c_side**2) == a_side**2):
        res = 'Right'
    elif b_side not in (a_side, c_side):
        res = 'Scalene'
    else:
        res = 'Isoceles'

    return res
    