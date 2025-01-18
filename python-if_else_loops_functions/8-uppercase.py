#!/usr/bin/python3
def uppercase(str):
    print_line = ""
    for i in str:
            if ord(i) > 96 and ord(i) < 123:
                  print_line += chr(ord(i) - 32)
            else:
                  print_line += i
    print("{}".format(print_line), end="")
    print("")