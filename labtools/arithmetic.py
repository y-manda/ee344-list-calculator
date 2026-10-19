"""Calculate a sum or product from a list of numbers."""
import numpy as np

def add(numbers):
    """Return the sum of the numbers; an empty list has sum 0."""
    total = 0
    for number in numbers:
        total = total + number
    return total

def multiply(numbers):
    """Return the product of the numbers; an empty list has product 1."""
    total = 1
    for number in numbers:
        total = total * number
    return total

def add_numpy(numbers):
    """Return the sum of numbers using numpy; an empty list has sum 0."""
    return np.sum(numbers)

def multiply_numpy(numbers):
    """Return the product of the numbers; an empty list has product 1."""
    return np.prod(numbers)