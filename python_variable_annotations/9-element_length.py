#!/usr/bin/env python3
""" function to compute sequence lengths """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns list of tuples with each sequence and its length """
    return [(i, len(i)) for i in lst]
