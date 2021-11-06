"""Checking if a string has matching delimiters

Author: Kevin Boyette
Date: 11/6/2021

"""
from typing import Deque
from collections import deque


def valid_delimiters(string: str) -> bool:
    """Check the string to see if the delimiters match.

    Valid delimiters are (, {, [, < and their closing tags.


    Args:
        string (str): A string to check

    Returns:
        bool: do the delimiters have a matching pair?

    """
    stack: Deque[str] = deque()
    delimiters = {"(": ")", "{": "}", "[": "]", "<": ">"}
    for char in string:
        if char in delimiters:
            stack.append(char)
        elif not stack or delimiters[stack.pop()] != char:
            return False
    return not stack
