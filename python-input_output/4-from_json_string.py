#!/usr/bin/python3
'''Write a function that returns an object
(Python data structure) represented by a JSON string:'''

import json


def from_json_string(my_str):
    '''returns the JSON representation of an string'''
    return json.loads(my_str)
