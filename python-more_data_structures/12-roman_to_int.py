#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    total = 0
    prev_value = 0
    ROMAN_NUMBER = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for symbol in roman_string:
        value = ROMAN_NUMBER.get(symbol, 0)
        if value == 0:
            return 0
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total
