#!/usr/bin/python3
'''class-checking function'''

def is_same_class(obj, a_class):
    '''Check if object is TRUE for instance or given class'''
    
    if type(obj) == a_class:
        return True
    return False
