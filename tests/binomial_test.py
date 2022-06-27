"""Tests for calculating binomial coefficients.

Author: Kevin Boyette
"""
from typing import Any
import itertools
import pytest
from algorithms import mathematics


@pytest.mark.parametrize(
    "name,inputs,expected",
    [
        ("positive value", 10, 3_628_800),
        ("testing 1", 1, 1),
        ("testing 2", 2, 2),
        ("testing 3", 3, 6),
        ("testing 5", 5, 120),
        ("testing 13", 13, 6_227_020_800),
        ("testing -1", -1, 1),
    ],
)
def test_factorial(name: str, inputs: int, expected: int) -> Any:
    """Test factorial function using the test table.

    Args:
        name (str): name of the test
        inputs (int): testing an integer input
        expected (int): value that is expected

    """
    assert expected == mathematics.factorial(inputs), name


small_binomial_coeffs = [
    ("10 choose 4", (10, 4), 210.0),
    ("10 choose 2", (10, 2), 45.0),
    ("20 choose 10", (20, 10), 184756.0),
    ("1 choose 1", (1, 1), 1),
    ("1 choose 0", (1, 0), 1),
]


@pytest.mark.parametrize("name,inputs,expected", small_binomial_coeffs)
def test_n_choose_r(name: str, inputs: tuple[int, int], expected: int) -> Any:
    """Test factorial function using the test table.

    Args:
        name (str): name of the test
        inputs (int): testing an integer input
        expected (int): value that is expected

    """
    assert expected == mathematics.n_choose_r(inputs[0], inputs[1]), name


@pytest.mark.parametrize(
    "name,inputs,expected",
    list(
        itertools.chain.from_iterable(
            [
                small_binomial_coeffs,
                [
                    ("100 choose 40", (100, 40), 1.3746234145802808e28),
                    ("1_000 choose 400", (1_000, 400), 4.9652723862542285e290),
                    # ("10_000 choose 4_000", (10_000, 4_000), 5.798629E+2920),
                ],
            ]
        )
    ),
)
def test_fast_binomial(
    name: str, inputs: tuple[int, int], expected: int
) -> Any:
    """Test factorial function using the test table.

    Args:
        name (str): name of the test
        inputs (int): testing an integer input
        expected (int): value that is expected

    """
    assert expected == mathematics.fast_binomial(inputs[0], inputs[1]), name
