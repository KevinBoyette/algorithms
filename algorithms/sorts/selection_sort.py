"""The SelectionSort Algorithm.

Author: Kevin Boyette
"""
from typing import List


def selection_sort(array: List[int]) -> List[int]:
    """Perform selection sort on a list.

    SelectionSort has a runtime of O(n**2).

    Args:
        array (List[int]): An array to be sorted

    Returns:
        List[int]: A sorted array

    """
    for i in range(len(array) - 1):
        ith_min = i
        for j in range(i, len(array)):
            if array[j] < array[ith_min]:
                ith_min = j
        array[i], array[ith_min] = array[ith_min], array[i]
    return array
