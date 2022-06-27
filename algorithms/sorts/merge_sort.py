"""The MergeSort Algorithm.

Author: Kevin Boyette
"""


def merge_sort(arr: list[int]) -> list[int]:
    """Sort an array using MergeSort.

        MergeSort has a worst case runtime of O(nlog(n)).
    MergeSort's best case uses roughly half as many iterations and
    is a stable sort.

    Args:
        arr (List[int]): An array to be sorted

    Returns:
        List[int]: A sorted array

    """
    arr_len = len(arr)
    if arr_len > 1:
        middle = arr_len // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return _merge(left, right)
    return list(arr)


def _merge(left: list[int], right: list[int]) -> list[int]:
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
