#!/usr/bin/env python3
""" a function that takes an int and returns a asyncio.Task """


import asyncio
wait_r = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """ a function that takes max_delay:int and returns a asyncio.Task """
    return asyncio.create_task(wait_r(max_delay))
