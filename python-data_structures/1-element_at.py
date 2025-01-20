#!/usr/bin/python3

def element_at(my_list, idx):
    if my_list[idx] < 0 or my_list[idx] > 4:
        return None
    return my_list[idx]
