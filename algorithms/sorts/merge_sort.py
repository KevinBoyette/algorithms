"""The MergeSort Algorithm.

Author: Kevin Boyette
"""
from typing import List
from array import array


def merge_sort(arr: List[int]) -> List[int]:
    """Sort an array using MergeSort.

        MergeSort has a worst case runtime of O(nlog(n)).
    MergeSort's best case uses roughly half as many iterations and
    is a stable sort.

    Args:
        arr (List[int]): An array to be sorted

    Returns:
        List[int]: A sorted array

    """
    temp = array("l", arr)
    temp_len = len(temp)
    if temp_len > 1:
        middle = temp_len // 2
        left = merge_sort(temp[:middle])
        right = merge_sort(temp[middle:])
        return _merge(left, right)
    return list(temp)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = array("l", [])
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
    return list(result)
