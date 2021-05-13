"""Tests for converting to camelCase.

Author: Kevin Boyette
"""
from typing import Any
import pytest
from algorithms.interview import to_camel_case


@pytest.mark.parametrize(
    "name,inputs,expected",
    [
        ("empty string", "", ""),
        ("the_stealthy_warrior", "the_stealthy_warrior", "theStealthyWarrior"),
        ("the-stealthy-warrior", "the-stealthy-warrior", "theStealthyWarrior"),
        ("Python_algorithms", "Python_algorithms", "PythonAlgorithms"),
    ],
)
def test_to_camel_case(name: str, inputs: str, expected: str) -> Any:
    """Test to_camel_case using the test table.

    Args:
        name (str): name of the test
        inputs (int): testing a string input
        expected (int): value that is expected
    """
    assert expected == to_camel_case(inputs), name
