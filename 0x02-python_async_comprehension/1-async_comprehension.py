#!/usr/bin/env python3
"""1-async_comporehension.py module"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from
    async_generator and returns them
    """

    return [_ async for _ in async_generator()]
