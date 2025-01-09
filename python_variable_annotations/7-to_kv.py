#!/usr/bin/env python3
""" type annotation function that takes a str, and an int or float and returns a tuple """


from typing import Union

def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """ function takes k as str, and v as int or float and returns a tuple """
    return k, float(v ** 2)
