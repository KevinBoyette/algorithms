"""The Fast Exponentiation Algorithm.

Author: Kevin Boyette
"""
from typing import Any


def _is_even(questionable_int: Any) -> bool:
    return bool(questionable_int % 2 == 0)


def _is_odd(questionable_int: Any) -> bool:
    return bool(questionable_int % 2 == 1)


def _is_negative(questionable_int: Any) -> bool:
    return bool(questionable_int < 0)


def _is_zero(questionable_int: Any) -> bool:
    return bool(questionable_int == 0)


def _is_one(questionable_int: Any) -> bool:
    return bool(questionable_int == 1)


def recursive_fast_exponentiation(base: Any, exponent: Any) -> Any:
    """Recursive method for computing x**n by squaring.

    Args:
        base (int): An integer base
        exponent (int): The exponent ontop of the base

    Returns:
        int: The result of base**exponent

    """
    if _is_zero(exponent):
        return 1
    if _is_negative(exponent):
        return recursive_fast_exponentiation(1 / base, -exponent)
    if _is_one(exponent):
        return base
    if _is_even(exponent):
        return recursive_fast_exponentiation(base * base, exponent / 2)
    #if _is_odd(exponent):
    return base * recursive_fast_exponentiation(
            base * base,
            (exponent - 1) / 2,
        )


def iterative_fast_exponentiation(base: Any, exponent: Any) -> Any:
    """Compute x**n by squaring by iterating.

    Args:
        base (int): An integer base
        exponent (int): The exponent ontop of the base

    Returns:
        int: The result of base**exponent

    """
    if _is_zero(exponent):
        return 1
    if _is_negative(exponent):
        base = 1 / base
        exponent = -exponent
    old_base = 1
    while exponent > 1:
        if _is_even(exponent):
            base *= base
            exponent /= 2
        else:
            old_base = base
            base *= base
            exponent = (exponent - 1) / 2
    return base * old_base
