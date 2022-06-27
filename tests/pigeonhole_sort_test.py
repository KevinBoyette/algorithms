"""Tests For Pigeonhole Sort.

Author: Kevin Boyette
"""

from typing import Any
from copy import deepcopy
import pytest
from algorithms import sorts

TEST_CASES = [
    ("empty list", [], []),
    ("single element", [(1, "test")], [(1, "test")]),
    (
        "two elements",
        [(2, "test"), (1, "item")],
        [
            (1, "item"),
            (2, "test"),
        ],
    ),
    (
        "reversed list",
        [
            (5, "test"),
            (4, "test"),
            (3, "test"),
            (2, "test"),
            (1, "test"),
        ],
        [
            (1, "test"),
            (2, "test"),
            (3, "test"),
            (4, "test"),
            (5, "test"),
        ],
    ),
    (
        "alternating values",
        [
            (5, "test"),
            (3, "test"),
            (4, "test"),
            (1, "test"),
            (2, "test"),
        ],
        [
            (1, "test"),
            (2, "test"),
            (3, "test"),
            (4, "test"),
            (5, "test"),
        ],
    ),
]


@pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
def test_pigeonhole_sort(
    name: str, inputs: list[tuple[int, str]], expected: list[tuple[int, str]]
) -> Any:
    """Test pigeonhole_sort using the test table.

    Args:
        name (str): name of the test
        inputs (List[Tuple[int, Any]]): testing a list of tuples
        expected (List[Tuple[int, Any]]): A sorted list of tuples

    """
    assert expected == sorts.pigeonhole_sort(inputs), name


def test_original_array_is_not_mutated() -> None:
    """Test that the original array is not mutated by our sort."""
    initial = [
        (5, "test"),
        (4, "test"),
        (3, "test"),
        (2, "test"),
        (1, "test"),
    ]
    expected = deepcopy(initial)
    sorts.pigeonhole_sort(initial)
    assert initial == expected
