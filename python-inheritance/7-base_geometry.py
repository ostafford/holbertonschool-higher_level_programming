#!/usr/bin/python3
'''Define a base geometry class BaseGeometry'''


class BaseGeometry:
    '''Represent base geometry'''

    def area(self):
        '''not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validate parameter as int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
