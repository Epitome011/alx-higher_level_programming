#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    Args:
        text: input string
    Returns:
        No return
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    d = text[:]

    for y in ".?:":
        list_text = d.split(y)
        d = ""
        for i in list_text:
            i = i.strip(" ")
            d = i + y if d is "" else d + "\n\n" + i + y

    print(d[:-3], end="")
