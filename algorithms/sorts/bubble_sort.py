"""The BubbleSort Algorithm.

Author: Kevin Boyette
"""
from typing import List
from array import array


def bubble_sort(arr: List[int]) -> List[int]:
    """Sort a list in O(n**2) time.

    Why would you ever need this sort?
    It's best used with the list is already sorted ;)

    Args:
        arr (List[int]): A list to be sorted
    Returns:
        List[int]: A sorted copy of the input list
    """
    temp = array("l", arr)
    temp_len = len(temp) - 1
    for _ in range(temp_len):
        for j in range(temp_len):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
    return list(temp)
