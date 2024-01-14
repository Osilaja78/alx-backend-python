#!/usr/bin/env python3
"""8-make_multiplier.py module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated make multiplier function
    Parameters:
        multiplier - float
    Return: callable function
    """

    def multiply(n: float):
        """Multiplies n by multiplier"""

        return n * multiplier
    return multiply
