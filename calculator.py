"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

import math

def add(a, b): a + b

def subtract(a, b): a - b

def multiply(a, b): a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if b <= 0 and a <= 1:
        raise ValueError()
    else:
        return loga(b)# use math library/raise ValueError

def exponent(a, b): a**b


