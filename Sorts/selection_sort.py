#!/usr/bin/env python3
# Kevin Boyette

# TODO add cool factor to docstring


def selection_sort(array):
    """

    Input: An array to be sorted
    Output: A sorted array

    Selection sort has a runtime of O(n**2).

    :param array:
    :return:
    """
    for i in range(len(array) - 1):
        ith_min = i
        for j in range(i, len(array)):
            if array[j] < array[ith_min]:
                ith_min = j
        array[i], array[ith_min] = array[ith_min], array[i]
    return array
