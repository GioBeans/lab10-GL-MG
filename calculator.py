"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if b <= 0 and a <= 1:
        raise ValueError
    else:
        return loga(b)# use math library/raise ValueError

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

