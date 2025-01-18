#!/usr/bin/python3
def uppercase(str):
    str_frame = ""
    for i in str:
            if ord(i) > 96 and ord(i) < 123:
                  str_frame += chr(ord(i) - 32)
            print("{}".format(str_frame), end="")
    print("")
