#!/usr/bin/python3


def is_even(n):
    return True if n % 2 == 0 else False


def is_odd(n):
    return True if n % 2 == 1 else False


def is_negative(n):
    return True if n < 0 else False


def is_zero(n):
    return True if n == 0 else False


def is_one(n):
    return True if n == 1 else False


def recur_exp_by_squaring(x, n):
    """
            Recursive method for computing x**n by
            squaring.

                     x(x**2)**(n-1)/2 if n is odd
                    /
            x**n = {
                    \
                     (x**2) **(n/2) if n is even

        """
    if is_zero(n):
        return 1
    elif is_negative(n):
        return recur_exp_by_squaring(1 / x, -n)
    elif is_one(n):
        return x
    elif is_even(n):
        return recur_exp_by_squaring(x * x, n / 2)
    elif is_odd(n):
        return x * recur_exp_by_squaring(x * x, (n - 1) / 2)


def iterative_squaring_exponent_method(x, n):
    """
        Iterative method for computing x**n by
        squaring.

                 x(x**2)**(n-1)/2 if n is odd
                /
        x**n = {
                \
                 (x**2) **(n/2) if n is even

    """

    if is_zero(n):
        return 1
    elif is_negative(n):
        x = 1 / x
        n = -n
    y = 1
    while n > 1:
        if is_even(n):
            x *= x
            n /= 2
        else:
            y = x * 1
            x *= x
            n = (n - 1) / 2
    return x * y
