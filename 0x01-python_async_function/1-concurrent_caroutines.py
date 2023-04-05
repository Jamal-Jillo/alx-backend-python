#!/usr/bin/env python3
""" 1. Let's execute multiple coroutines at the same time with async """


import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for a random delay between 0 and max_delay."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    completed, _ = await asyncio.wait(coroutines)
    delays = [task.result() for task in completed]
    return sorted(delays)
