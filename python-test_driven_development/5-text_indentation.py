#!/usr/bin/python3
"""This module reprsents how to define text indentation"""


def text_indentation(text):
    """
      Text Indentation

      Print: Final Result of text indentation

      Possible Error:
      TypeError: based on type of text


    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ''
    n = len(text)
    i = 0

    while i < n:
        result += text[i]
        if text[i] in ['.', '?', ':']:
            result += '\n\n'
            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1

    result_lines = result.split('\n')
    stripped_lines = [line.strip() for line in result_lines]
    final_result = '\n'.join(stripped_lines)

    print(final_result, end='')
