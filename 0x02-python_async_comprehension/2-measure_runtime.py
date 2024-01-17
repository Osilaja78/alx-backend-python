#!/usr/bin/env python3
"""2-measure_runtime.py module"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of async_comprehension"""

    s = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    e = time.perf_counter()

    return e - s
