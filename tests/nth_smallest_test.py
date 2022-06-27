"""Tests For Nth Smallest.

Author: Kevin Boyette
"""
from typing import Any

import pytest

from algorithms.misc import nth_smallest


TEST_CASES = [
    # ("empty list", [], 0, None),
    ("single element", [1], 1, 1),
    ("two elements", [2, 1], 2, 2),
    ("reversed list", [5, 4, 3, 2, 1], 3, 3),
    ("alternating values", [5, 3, 4, 1, 2], 4, 4),
]


@pytest.mark.parametrize(
    "test_name,input_array,test_parameter,expected_value",
    TEST_CASES,
)
def test_nth_smallest(
    test_name: str,
    input_array: list[int],
    test_parameter: int,
    expected_value: int,
) -> Any:
    """Test for the nth smallest integer in an unsorted array.

    Args:
        test_name (str):            The name of the test
        input_array (list[int]):    Testing an array of ints
        test_parameter (int):       The nth smallest integer to find
        expected_value (list[int]): The nth smallest integer from the array

    """
    assert expected_value == nth_smallest(
        input_array,
        test_parameter,
    ), test_name
