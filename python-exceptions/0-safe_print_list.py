#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = []
    count = 0
    i = 0
    while i < x:
        try:
            element = my_list[i]
            printed_elements.append(str(element))
            count += 1
            i += 1
        except IndexError:
            break
    print(''.join(printed_elements))
    return count
