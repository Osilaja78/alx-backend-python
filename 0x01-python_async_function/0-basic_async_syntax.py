#!/usr/bin/env python3
"""0-basic_async_syntax.py module"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay time between 0 and max_delay"""

    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
