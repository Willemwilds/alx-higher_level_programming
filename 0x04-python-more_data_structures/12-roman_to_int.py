#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_num = {
                    'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000
                }
    total = 0
    init_value = 0

    for num in reversed(roman_string):
        value = roman_num.get(num, 0)
        if value >= init_value:
            total += value
        else:
            total -= value
        init_value = value

    return total
