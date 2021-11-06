"""Tests for validating delimiters in a string.

Author: Kevin Boyette
"""
from typing import Any
import pytest
from algorithms import strings

TEST_CASES = [("()", True), ("([])", True), ("()[]{}", True), ("[[", False)]


@pytest.mark.parametrize("inputs,expected", TEST_CASES)
def test_valid_demimiters(inputs: str, expected: bool) -> Any:
    """Test that input strings have matching delimiters.

    Args:
        inputs (str): example strings for testing
        expected (bool): expected result
    """
    assert expected == strings.valid_delimiters(inputs), inputs
