#!/usr/bin/python3

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
    if n == 0:
        return 1
    elif n < 0:
        return recur_exp_by_squaring(1/x, -n)
    elif n == 1:
        return x
    elif n % 2 == 0:
        return recur_exp_by_squaring(x*x, n/2)
    elif n % 2 == 1:
        return x * recur_exp_by_squaring(x *x, (n - 1)/ 2)


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
    if n == 0:
        return 1
    elif n < 0:
        x = 1/x
        n = -n

    y = 1
    while n > 1:
        if n % 2 == 0:
            x *= x
            n /= 2
        else:
            y = x * 2
            x *= x
            n = (n - 1) / 2
    return x * y
