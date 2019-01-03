# -*- coding: utf-8 -*-
"""reverse.py.

Author: Kevin Boyette
"""


def reverse(string: str) -> str:
    """Reverse a string.

    Args:
        string (str): A string/word

    Returns:
        str: the reverse of the given string

    """
    word_len = len(string)
    if word_len <= 1:
        return string
    characters = list(string)
    left_index = 0
    right_index = word_len - 1
    while left_index < word_len / 2:
        characters[left_index], characters[right_index] = (
            characters[right_index],
            characters[left_index],
        )
        left_index += 1
        right_index -= 1
    return "".join(characters)
