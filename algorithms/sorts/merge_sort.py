# -*- coding: utf-8 -*-
"""The MergeSort Algorithm.

Author: Kevin Boyette
"""
from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """Sort an array using MergeSort.

        MergeSort has a worst case runtime of O(nlog(n)).
    MergeSort's best case uses roughly half as many iterations and
    is a stable sort.

    Args:
        array (List[int]): An array to be sorted

    Returns:
        List[int]: A sorted array

    """
    array_len = len(array)
    if array_len > 1:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return _merge(left, right)
    return array


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    left_length = len(left)
    right_length = len(right)
    while left_length > 0 and right_length > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
        left_length = len(left)
        right_length = len(right)

    new_left_length = len(left)
    if new_left_length != 0:
        result.extend(left)
    result.extend(right)
    return result
