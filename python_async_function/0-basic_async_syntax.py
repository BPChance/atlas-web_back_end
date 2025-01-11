#!/usr/bin/env python3
""" asynchronous coroutine that waits for a delay and returns it """


import random, asyncio


async def wait_random(max_delay: int) -> float:
    """ asynchronous coroutine that waits for a random delay and returns it """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
