#!/usr/bin/python3
def uppercase(str):
    str_frame = ""
    for i in str:
            if ord(i) > 96 and ord(i) < 123:
                  str_frame += chr(ord(i) - 32)
            else:
                  str_frame += i
    print("{}".format(str_frame), end="")
    print("")
    