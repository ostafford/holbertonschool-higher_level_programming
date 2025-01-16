#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig_str = "Last digit of"
last_num = number%10

if last_num > 5:
    print(last_dig_str, number, "is", last_num, "and is greater than 5")
elif last_num == 0:
    print(last_dig_str, number, "is", last_num, "and is 0")
else:
    print(last_dig_str, number, "is", last_num, "and is les than 6 and not 0")