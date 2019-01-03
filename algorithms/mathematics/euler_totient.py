# -*- coding: utf-8 -*-
"""Euler's Totient/Phi Function.

Author: Kevin Boyette
"""
from typing import Any


def euler_totient(positive_int: Any) -> Any:
    """Find the num of integers relatively prime to a given positive integer.

    Euler's Totient Function counts the positive integers up to
    a given integer n that are 'relatively' prime to n.

    Usually denoted with the greek symbol for phi.

    Args:
        positive_int (int): A positive integer

    Returns:
        int: The number of integers relatively prime to n

    Example:
        euler_totient(10) == 4
          (1, 3, 7, 9) are less than 10,
          but have no common factors with 10

    Example:
        euler_totient(9) == 6
          (1, 2, 4, 5, 7, 8) are less than 10,
          but have no common factors with 9

    Example:
        euler_totient(5) == 4
            (1, 2, 3, 4) are less than 5 and since 5 is prime,
            all the numbers less than 5 are relatively prime to 5.

    """
    result = positive_int
    prime = 2
    while prime * prime <= positive_int:
        if positive_int % prime == 0:
            while positive_int % prime == 0:
                positive_int /= prime
            result *= 1.0 - (1.0 / float(prime))
        prime += 1

    if positive_int > 1:
        result *= 1.0 - (1.0 / float(positive_int))
    return int(result)
