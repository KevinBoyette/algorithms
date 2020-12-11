"""The InsertionSort Algorithm.

Author: Kevin Boyette

Insertion sort, nothing fancy and pretty standard
"""
from typing import List
from array import array


def insertion_sort(arr: List[int]) -> List[int]:
    """Sort an arr using InsertionSort.

        Insertion sort has a runtime of O(n**2).
    A runtime of O(n) is achievable if the arr is
    almost sorted.

    Args:
        arr (List[int]): An array to be sorted

    Returns:
        List[int]: A sorted array

    """
    temp = array("l", arr)
    temp_len = len(temp)
    for i in range(1, temp_len):
        element = temp[i]
        j = i - 1
        while j >= 0 and temp[j] > element:
            temp[j + 1] = temp[j]
            j -= 1
            temp[j + 1] = element
    return list(temp)
