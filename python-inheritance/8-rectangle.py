#!/usr/bin/python3
'''Defines class rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    '''represents rectangle using BaseGeometry'''

    def __init__(self, width, height):
        '''initialize for new Rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
