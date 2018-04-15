# -*- coding: utf-8 -*-
"""simple_compression.py.

Author: Kevin Boyette
"""


def simple_compression(sequence: str) -> str:
    """Compress a string by counting character occurences.

    Args:
        sequence (str): A string/word

    Returns:
        str:  A compressed sequence of letters and counts

    Example:
        simple_compression('aaabbc') -> 'a3b2c1'

    """
    sequence_length = len(sequence)
    sequence = sequence.lower()
    if sequence_length < 1:
        return sequence
    elif sequence_length == 1:
        return sequence + '1'
    current_character = sequence[0]
    count = 1
    compressed_sequence = []
    for index in range(1, sequence_length):
        if sequence[index] == current_character:
            count += 1
        else:
            compressed_sequence.append(current_character + str(count))
            current_character = sequence[index]
            count = 1
    compressed_sequence.append(current_character + str(count))
    return ''.join(compressed_sequence)
