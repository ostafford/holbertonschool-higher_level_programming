#!/usr/bin/python3

'''Write a function that returns the dictionary description
with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:'''


argv = __import__('sys').argv
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []
items.extend(argv[1:])
save_to_json_file(items, filename)
