#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions """


import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ 2. Run time for four parallel comprehensions """
    start = asyncio.create_task(async_comprehension())
    end = asyncio.create_task(async_comprehension())
    return await asyncio.gather(start, end)
