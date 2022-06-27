"""Tests For Sorting Functions.

Author: Kevin Boyette
"""
from typing import Any

import pytest

from algorithms import sorts

TEST_CASES = [
    ("empty list", [], []),
    ("single element", [1], [1]),
    ("two elements", [2, 1], [1, 2]),
    ("reversed list", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ("alternating values", [5, 3, 4, 1, 2], [1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
def test_bubble_sort(name: str, inputs: list[int], expected: list[int]) -> Any:
    """Test BubbleSort using the test table.

    Args:
        name (str):  name of the test
        inputs (list[int]): testing a list of ints
        expected (list[int]): A sorted list of ints

    """
    assert expected == sorts.bubble_sort(inputs), name


@pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
def test_insertion_sort(
    name: str,
    inputs: list[int],
    expected: list[int],
) -> Any:
    """Test InsertionSort using the test table.

    Args:
        name (str): name of the test
        inputs (list[int]): testing a list of ints
        expected (list[int]): A sorted list of ints

    """
    assert expected == sorts.insertion_sort(inputs), name


@pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
def test_heap_sort(name: str, inputs: list[int], expected: list[int]) -> Any:
    """Test HeapSort using the test table.

    Args:
        name (str): name of the test
        inputs (list[int]): testing a list of ints
        expected (list[int]): A sorted list of ints

    """
    assert expected == sorts.heap_sort(inputs), name


@pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
def test_merge_sort(name: str, inputs: list[int], expected: list[int]) -> Any:
    """Test MergeSort using the test table.

    Args:
        name (str): name of the test
        inputs (list[int]): testing a list of ints
        expected (list[int]): A sorted list of ints

    """
    assert expected == sorts.merge_sort(inputs), name


@pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
def test_selection_sort(
    name: str,
    inputs: list[int],
    expected: list[int],
) -> Any:
    """Test SelectionSort using the test table.

    Args:
        name (str): name of the test
        inputs (list[int]): testing a list of ints
        expected (list[int]): A sorted list of ints

    """
    assert expected == sorts.selection_sort(inputs), name


# @pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
# def test_quick_sort(name, inputs, expected):
#     assert expected == sorts.quick_sort(inputs), name
