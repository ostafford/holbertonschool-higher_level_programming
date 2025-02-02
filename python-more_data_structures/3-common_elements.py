#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        raise TypeError("Arguments must be sets.")
    return set_1 & set_2
