""" Provides a function to compute factorial.
"""

def factorial(n):
    f = 1
    for i in range(n):
        f *= i + 1
    return f
