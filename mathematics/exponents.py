#!/usr/bin/python3


def _is_even(n): return True if n % 2 == 0 else False


def _is_odd(n): return True if n % 2 == 1 else False


def _is_negative(n): return True if n < 0 else False


def _is_zero(n): return True if n == 0 else False


def _is_one(n): return True if n == 1 else False


def recur_exp_by_squaring(x, n):
    """
            Recursive method for computing x**n by
            squaring.
    """
    if _is_zero(n):
        return 1
    elif _is_negative(n):
        return recur_exp_by_squaring(1 / x, -n)
    elif _is_one(n):
        return x
    elif _is_even(n):
        return recur_exp_by_squaring(x * x, n / 2)
    elif _is_odd(n):
        return x * recur_exp_by_squaring(x * x, (n - 1) / 2)


def iterative_squaring_exponent_method(x, n):
    """ 
        Iterative method for computing x**n by
        squaring.
    """

    if _is_zero(n):
        return 1
    elif _is_negative(n):
        x = 1 / x
        n = -n
    y = 1
    while n > 1:
        if _is_even(n):
            x *= x
            n /= 2
        else:
            y = x * 1
            x *= x
            n = (n - 1) / 2
    return x * y
