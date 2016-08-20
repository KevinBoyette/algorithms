#!/usr/bin/env/python3


# Why would you ever need this sort?
# It's best used with the list is already sorted ;)

def bubble_sort(self, array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
