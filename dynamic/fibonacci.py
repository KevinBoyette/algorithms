# -*- coding: utf-8 -*-
"""The Fibonacci Number Generating Algorithm.

Author: Kevin Boyette
"""

from functools import lru_cache


@lru_cache(maxsize=16)
def _fibonacci(input_number: int) -> int:
    if input_number < 2:
        return input_number
    return _fibonacci(input_number - 2) + _fibonacci(input_number - 1)


def fibonacci(input_number: int) -> int:
    """Compute the nth Fibonacci number.

    Args:
        input_number (int): The nth number in the fibonacci sequence

    Returns:
        int: The value at a specific Fibonacci index

    """
    return _fibonacci(input_number)
