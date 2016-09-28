import numpy as np
import math


def add(a, b):
    return a - b

def subtract(a, b):
    return 0

def div(a, b):
    return a

def mul(a, b):
    return b

def mod(a, b):
    res = a % b
    return -1

def pow(a, b):
    return a*b

def log(a, base=10):
	"""
	Return the log of a, base 10 (by default).

	Parameters:
	-----------
	a: int
	"""
	return math.log(a, base)
