"""The SelectionSort Algorithm.

Author: Kevin Boyette
"""
from array import array


def selection_sort(arr: list[int]) -> list[int]:
    """Perform selection sort on a list.

    SelectionSort has a runtime of O(n**2).

    Args:
        arr (List[int]): An array to be sorted

    Returns:
        List[int]: A sorted array

    """
    temp = array("l", arr)
    temp_len = len(arr) - 1
    for i in range(temp_len):
        ith_min = i
        for j in range(i, temp_len):
            if temp[j] < temp[ith_min]:
                ith_min = j
        temp[i], temp[ith_min] = temp[ith_min], temp[i]
    return list(temp)
