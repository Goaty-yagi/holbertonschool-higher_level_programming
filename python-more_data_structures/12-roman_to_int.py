#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    total = 0
    ROMAN_NUMBER = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for i in range(len(roman_string)):
        if roman_string[i] in ("X", "V"):
            if (i > 0 and roman_string[i-1] == "I"):
                total -= 2
        total += ROMAN_NUMBER[roman_string[i]]

    return total
