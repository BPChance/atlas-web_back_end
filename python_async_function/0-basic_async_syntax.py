#!/usr/bin/env python3
""" asynchronous coroutine that waits for a delay and returns it """


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine that waits for a random delay and returns it """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
