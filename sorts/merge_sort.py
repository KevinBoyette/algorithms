#!/usr/bin/python3
# MergeSort
# Kevin Boyette


def merge_sort(array):
    array_len = len(array)
    if array_len > 1:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return _merge(left, right)
    return array


def _merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) != 0:
        result.extend(left)
    else:
        result.extend(right)
    return result
