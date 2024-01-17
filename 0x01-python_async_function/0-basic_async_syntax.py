#!/usr/bin/env python3
"""0-basic_async_syntax.py module"""

import asyncio
import random


async def wait_random(max_delay=10):
    """waits for a random delay time between 0 and max_delay"""

    d = random.uniform(0, max_delay)
    await asyncio.sleep(d)
    return d
