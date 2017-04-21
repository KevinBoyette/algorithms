#!/usr/bin/python3


def isEven(n): return True if n % 2 == 0 else False


def isOdd(n): return True if n % 2 == 1 else False


def isNegative(n): return True if n < 0 else False


def isZero(n): return True if n == 0 else False


def isOne(n): return True if n == 1 else False


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
    if isZero(n):
        return 1
    elif isNegative(n):
        return recur_exp_by_squaring(1 / x, -n)
    elif isOne(n):
        return x
    elif isEven(n):
        return recur_exp_by_squaring(x * x, n / 2)
    elif isOdd(n):
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
    print("x: {} n:{}".format(x, n))
    if isZero(n):
        return 1
    elif isNegative(n):
        x = 1 / x
        n = -n
    y = 1
    while n > 1:
        if isEven(n):
            x *= x
            n /= 2
        else:
            y = x * 1
            x *= x
            n = (n - 1) / 2
    return x * y
