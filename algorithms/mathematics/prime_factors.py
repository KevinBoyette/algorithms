"""Prime Factorization.

Author: Kevin Boyette
"""
from math import sqrt
from typing import Any


def prime_factorization(natural_number: Any) -> list[int]:
    """Find all prime factors of a given natural number.

    Args:
        natural_number (int): A natural number to factor

    Returns:
        List[int]: A list of prime factors of natural_number

    """
    if natural_number <= 1:
        return []
    prime_factors = []
    while natural_number % 2 == 0:
        prime_factors.append(2)
        natural_number /= 2
    for next_num in range(3, int(sqrt(natural_number)) + 1, 2):
        while natural_number % next_num == 0:
            prime_factors.append(int(next_num))
            natural_number /= next_num
    if natural_number > 2:
        prime_factors.append(int(natural_number))
    return prime_factors
