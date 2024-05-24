#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    prev_value = 0

    for char in roman_string:
        value = roman_numerals[char]
        if value == 0:
            return None

        if value > prev_value:
            integer_value += value - 2 * prev_value
        else:
            integer_value += value
        prev_value = value
    return integer_value
