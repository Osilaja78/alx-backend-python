#!/usr/bin/env python3
"""2-measure_runtime.py module"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total exec time for wait_n
    Returns total_time / n
    """

    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    e = time.perf_counter()

    total_time = e - s
    return total_time / n
