#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string):
        return (0)
    res_int = 0
    a_dictionary = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500,
                    'M': 1000}
    temp = ()
    for c in roman_string:
        if len(temp) == 0:
            temp = c
        for r in a_dictionary:
            if c == r:
                if a_dictionary[temp] < a_dictionary[c]:
                    res_int -= a_dictionary[temp] * 2
                res_int += a_dictionary[c]
                temp = r
                break
    return (res_int)
