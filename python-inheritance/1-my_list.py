#!/usr/bin/python3
'''inherit list from class MyList'''


class MyList(list):
    '''sort printing for the built-in list class'''
    def print_sorted(self):
        print(sorted(self))
