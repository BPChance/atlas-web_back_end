#!/usr/bin/env python3
"""
type annotated function that takes a list of
ints and floats and returns their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function that takes list of ints and floats and returns a float """
    return sum(mxd_lst)
