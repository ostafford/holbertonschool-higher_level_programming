#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    total = 0
    for i in range(len(roman_string)):
        current = roman_values[roman_string[i]]
        if i < len(roman_string) - 1:
            next_val = roman_values[roman_string[i+1]]
            if current < next_val:
                total -= current
            else:
                total += current
        else:
            total += current
    return total
