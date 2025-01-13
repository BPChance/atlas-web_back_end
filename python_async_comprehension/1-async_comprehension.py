#!/usr/bin/env python3
""" asynchronous comprehension function that collects random numbers """


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using async comprehension
    over async_generator and returns them as a list
    """
    list_numbers = [value async for value in async_generator()]
    return list_numbers
