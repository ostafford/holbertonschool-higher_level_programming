#!/usr/bin/python3
'''Defines class adn inherits class function'''


def is_kind_of_class(obj, a_class):
    '''checking if object is instance or inherited from parent class '''
    if isinstance(obj, a_class):
        return True
    return False

    # return isinstance(obj, a_class): <- Shorthand Version
