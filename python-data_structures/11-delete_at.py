#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    try:
        del my_list[idx]
    except (IndexError, TypeError):
        pass
    return my_list
