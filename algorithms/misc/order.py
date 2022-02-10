"""https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
Author: Kevin Boyette
"""


def order(sentence: str) -> str:
    """
    Reorder the sentence based on the numbers inside the words in the sentence.

    Args:
        sentence: a sentence to be reordered

    Returns:
        A sorted sentence

    """
    return " ".join(
        sorted(sentence.split(), key=lambda x: next(filter(str.isdigit, x)))
    )
