#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_num = my_list[0]
    for num in my_list[1:]:
        if num > max_num:
            max_num = num
    return max_num

# check if list is empty - return NONE
# Set starting point of list (max_num)
# Start the iteration through the list of numbers with for loop
# set the condition of if iteration (num) is bigger than the starting point (max_num)
# set max_num to num
# return the highest value. 
