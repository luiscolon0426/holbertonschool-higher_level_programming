#!/usr/bin/python3
"""

Text indentation

"""


def text_indentation(text):
    """
    print text with 2 new lines after each specified char
    """

    error1 = "text must be a string"
    if type(text) is not str:
        raise TypeError(error1)

    brk = True
    for i in text.strip():
        if brk and i == ' ':
            continue
        print(i, end="")
        brk = False
        if i in ['.', '?', ':']:
            print('\n')
            brk = True
