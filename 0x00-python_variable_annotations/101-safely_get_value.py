#!/usr/bin/env python3
"""101-safely_get_value.py module"""

from typing import Any, Mapping, Union, TypeVar
T = TypeVar('T')


def safely_get_value(
            dct: Mapping,
            key: Any,
            default: Union[T, None] = None
        ) -> Union[Any, T]:
    """More involved type annotations"""

    if key in dct:
        return dct[key]
    else:
        return default
