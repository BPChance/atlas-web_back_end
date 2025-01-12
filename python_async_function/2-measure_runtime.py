#!/usr/bin/env python3
"""
function that takes n and max_delay as arguments and
measures total execution time and returns the average as a float
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    takes n: int and max_delay: int and measures
    execution time and returns the average as a float
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    execution_time = end_time - start_time
    avg_time = execution_time / n
    return avg_time
