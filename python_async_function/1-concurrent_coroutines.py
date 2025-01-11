#!/usr/bin/env python3
""" async function that gathers mutiple random delays """


wait_r = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times with max_delay
    and returns list of delays ascending
    """
    delays = []
    tasks = [wait_r(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
