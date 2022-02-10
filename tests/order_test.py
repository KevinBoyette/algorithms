"""Tests For CodeWars' Order."""

from typing import Any
import pytest
from algorithms.misc import order

TEST_CASES = [
    ("first case", "is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"),
    (
        "second case",
        "4of Fo1r pe6ople g3ood th5e the2",
        "Fo1r the2 g3ood 4of th5e pe6ople",
    ),
    ("third case", "", ""),
]


@pytest.mark.parametrize(
    "name,param,expected",
    TEST_CASES,
)
def test_order(name: str, param: str, expected: str) -> Any:
    """Test for ordering a sentence on numbered words.

    Args:
        name:   the name of the test
        param:  the parameter to be tested
        expected:  the expected result

    Returns:
        A passing or failing test

    """
    assert expected == order(param), name
