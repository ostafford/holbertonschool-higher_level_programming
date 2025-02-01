#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    try:
        return my_list[:idx] + my_list[idx+1:]
    except (IndexError, TypeError):
        return my_list.copy()
