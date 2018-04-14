# -*- coding: utf-8 -*-
"""The BubbleSort Algorithm.

Author: Kevin Boyette
"""
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """Sort a list in O(n**2) time.

    Why would you ever need this sort?
    It's best used with the list is already sorted ;)

    Args:
        array (List[int]): A list to be sorted
    Returns:
        List[int]: A sorted copy of the input list
    """
    for _ in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
