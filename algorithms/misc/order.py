"""https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
Author: Kevin Boyette
"""


def _position(word: str) -> int:
    """
    Find where the number occurs in the word

    Args:
        word: a word that contains a number inside it

    Returns:
        int: the position in which the number occurs

    """

    pos = (int(number) for number in word if number.isdigit())
    return next(pos)


def order(sentence: str) -> str:
    """
    Reorder the sentence based on the numbers inside the words in the sentence.

    Args:
        sentence: a sentence to be reordered

    Returns:
        A sorted sentence

    """
    if len(sentence) <= 1:
        return sentence
    split = sentence.split(" ")
    result = [""] * (len(split) + 1)
    for word in split:
        result[_position(word)] = word

    return " ".join(word for word in result if word != "")
