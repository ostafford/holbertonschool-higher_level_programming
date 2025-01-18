#!/usr/bin/python3
for digit_1 in range(0, 10):
    for digit_2 in range(0, 10):
        if digit_1 >= digit_2:
            continue
        if digit_1 * digit_2 != 72:
            print("{}{}".format(digit_1, digit_2), end=", ")
        else:
            print("{}{}".format(digit_1, digit_2))
