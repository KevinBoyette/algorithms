#!/usr/bin/env/python3

# Insertion sort, nothing fancy and pretty standard


def insertion_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = x
    return array
