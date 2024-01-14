#!/usr/bin/env python3
"""6-sum_mixed_list.py module"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up a mixture of ints and floats in a list.
    Parameters:
        mxd_lst - mixed list of float and int.
    Return: sum of mxd_lst
    """

    return sum(mxd_lst)
