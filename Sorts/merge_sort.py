#!/usr/bin/python3
# MergeSort
# Kevin Boyette


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left = []
        right = []
        middle = len(array) // 2
        for eachLeftOfMiddle in array[:middle]:
            left.append(eachLeftOfMiddle)
        for eachRightOfMiddle in array[middle:]:
            right.append(eachRightOfMiddle)
        left = merge_sort(left)
        right = merge_sort(right)
        if left[-1] <= right[0]:
            left.extend(right)
            return left
        result = merge(left, right)
        return result


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result
