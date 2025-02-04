#!/usr/bin/python3
'''Define inherited class function'''


def inherits_from(obj, a_class):
    ''' check if object is inherited instance of class'''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
