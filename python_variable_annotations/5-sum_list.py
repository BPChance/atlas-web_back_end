#!/usr/bin/env python3
""" type annotated function that takes a list of floats and returns their sum as a float """


from typing import List

def sum_list(input_lists: List[float]) -> float:
    """ takes a list of floats and returns the sum as a float """
    return sum(input_lists)
