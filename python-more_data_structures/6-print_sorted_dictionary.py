#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not isinstance(a_dictionary, dict):
        raise TypeError("Input must be a dictionary.")
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")
