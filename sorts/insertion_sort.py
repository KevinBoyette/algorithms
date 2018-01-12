#!/usr/bin/env/python3

# Insertion sort, nothing fancy and pretty standard


def insertion_sort(array):
    """

    Input: An array to be sorted
    Output: A sorted array

    Insertion sort has a runtime of O(n**2).

    A runtime of O(n) is achievable if the array is almost sorted.

    :param array:
    :return:
    """

    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = x
    return array
