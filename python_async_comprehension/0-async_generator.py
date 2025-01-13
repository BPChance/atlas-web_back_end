#!/usr/bin/env python3
""" asynchronous generator that yields a random number """


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """ yields 10 numbers 1-10 at random with 1s delay """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
