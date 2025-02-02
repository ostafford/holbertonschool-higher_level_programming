#!/usr/bin/python3
def number_keys(a_dictionary):
    if not isinstance(a_dictionary, dict):
        raise TypeError("Input must be a dictionary.")
    return len(a_dictionary)
