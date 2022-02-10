""" Convert string from some case to CamelCase

Author: Kevin Boyette
"""

from io import StringIO
from typing import Tuple


def to_camel_case(string: str, predicate: Tuple[str, str] = ("_", "-")) -> str:
    """Convert string from snake_case or kebob-case to camelCase

    Args:
        string:         a string to convert

    Returns:
        str             a camelCase string

    Examples:
        to_camel_case("hello_world") -> "helloWorld"
        to_camel_case("Hello-World") -> "HelloWorld"
    """

    if len(string) < 1:
        return string

    string_builder = StringIO()
    string_builder.write(string[0])
    iterator = enumerate(string[1:])

    for index, char in iterator:
        # index is -1 from what we'd expect
        # due to slicing from [1:]
        # this means the next char is +2
        filtered = char in predicate
        text = string[index + 2].upper() if filtered else char
        if filtered:
            next(iterator, None)  # This feels gross
        string_builder.write(text)

    return string_builder.getvalue()
