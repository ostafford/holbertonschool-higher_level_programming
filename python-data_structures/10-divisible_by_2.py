#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result

# create an empty list
# iterate the value through the input (my_list)
# if the input (num) == 0 (being divisible by 2)
# append TRUE
# else FALSE
# return the boolean to the empty list (result)
