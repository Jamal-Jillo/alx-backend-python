#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions """

import time
from typing import List
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)."""
    start_time = time.monotonic()
    delays: List[float] = asyncio.run(wait_n(n, max_delay))
    total_time = time.monotonic() - start_time
    return total_time / n
