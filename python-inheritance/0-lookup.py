#!/usr/bin/python3
'''
Define object attribute lookup function
'''


def lookup(obj):
    '''
    Return list of objects from attribute if available
    '''
    return (dir(obj))
