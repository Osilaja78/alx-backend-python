#!/usr/bin/env python3
"""0-async_generator.py module"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """A coroutine that loops 10 times to yield a random no."""

    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
