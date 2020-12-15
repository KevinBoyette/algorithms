"""The MergeSort Algorithm.

Author: Kevin Boyette
"""
from typing import List, Union, TypeVar
from array import array

IntSequence = TypeVar("IntSequence", List[int], array[int])


def merge_sort(arr: IntSequence) -> List[int]:
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
    arr_len = len(temp)
    if arr_len > 1:
        middle = arr_len // 2
        left = merge_sort(temp[:middle])
        right = merge_sort(temp[middle:])
        return _merge(left, right)
    return list(arr)


def _merge(left: IntSequence, right: IntSequence) -> List[int]:
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
