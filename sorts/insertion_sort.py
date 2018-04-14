# -*- coding: utf-8 -*-
"""The InsertionSort Algorithm.

Author: Kevin Boyette

Insertion sort, nothing fancy and pretty standard
"""
from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    """Sort an array using InsertionSort.

        Insertion sort has a runtime of O(n**2).
    A runtime of O(n) is achievable if the array is
    almost sorted.

    Args:
        array (List[int]): An array to be sorted

    Returns:
        List[int]: A sorted array

    """
    for i in range(1, len(array)):
        element = array[i]
        j = i - 1
        while j >= 0 and array[j] > element:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = element
    return array
