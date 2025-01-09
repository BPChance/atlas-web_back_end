#!/usr/bin/env python3
"""
type annotated function that takes a str,
and an int or float and returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function takes k as str, and v as int or float and returns a tuple """
    return k, float(v ** 2)
