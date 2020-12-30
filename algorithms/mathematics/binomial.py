"""Algorithms for computing binomial coefficients.

Author: Kevin Boyette
"""


def factorial(number: int) -> int:
    """Calculate the factorial of a positive integer.

    Args:
        number (int): a positive integer

    Returns:
        int: the result of n * (n -1) * (n - 2) ... * 1
    """
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def n_choose_r(total_amount: int, chosen_amount: int) -> float:
    """Calculate C(n, r) recursively.

    Args:
        total_amount (int): total number of items in a set
        chosen_amount (int): number of items chosen from the set

    Returns:
        int:  The result of C(n, r)
    """
    return factorial(total_amount) / (
        factorial(chosen_amount) * factorial(total_amount - chosen_amount)
    )


def fast_binomial(total_amount: int, chosen_amount: int) -> float:
    """Calculate C(n, r) iteratively.

    Args:
        total_amount (int): total number of items in a set
        chosen_amount (int): number of items chosen from the set

    Returns:
        int:  The result of C(n, r)
    """
    result: float = 1.0
    if chosen_amount > (total_amount - chosen_amount):
        chosen_amount = total_amount - chosen_amount
    for i in range(0, chosen_amount):
        result *= total_amount - i
        result /= i + 1
    return result
