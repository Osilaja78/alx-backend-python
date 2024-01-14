#!/usr/bin/env python3
"""7-to_kv.py module"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and int or float as arg and return tuple.
    Parameters:
        k - string
        v - int or float
    Return: tuple(k, v squared)
    """

    return (k, v ** 2)
