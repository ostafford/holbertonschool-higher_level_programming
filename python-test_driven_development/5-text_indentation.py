#!/usr/bin/python3
"""
Module for text indentation.
Contains a function that formats text with special characters.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = text.replace(delim, delim + "\n\n")

    lines = text.split("\n")
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            print(line.strip(), end="")
        else:
            print(line.strip())
