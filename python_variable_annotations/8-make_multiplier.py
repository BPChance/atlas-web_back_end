#!/usr/bin/env python3
"""type annotated function that takes a float and
returns a function that multiplies it by a float
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """
    def float_multiplier(n: float) -> float:
        return n * multiplier
    return float_multiplier
