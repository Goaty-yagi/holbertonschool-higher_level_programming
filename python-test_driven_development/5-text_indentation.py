#!/usr/bin/python3

"""

This module defines a function for splitting a given text into
paragraphs based on the presence of '.', '?', or ':' characters.

Usage:
    from text_processor import text_indentation

    example_text = "This is a sample text. It has multiple sentences.
    Each ends with a period."
    text_indentation(example_text)
"""


def text_indentation(text):
    """
    Splits the input text into paragraphs based on the
    presence of '.', '?', or ':' characters.

    Parameters:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input 'text' is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start_index = 0

    for i in range(len(text)):
        if text[i] in (".", "?", ":"):
            print(text[start_index: i + 1].strip(), end="\n\n")
            start_index = i + 1
    print(text[start_index: len(text)].strip(), end="")
