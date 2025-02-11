#!/usr/bin/python3
'''Write a function that creates
an Object from a “JSON file”:'''

import json

def load_from_json_file(filename):
    '''creates an Object from a “JSON file”'''
    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(filename, f)
