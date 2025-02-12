#!/usr/bin/python3
import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items or create empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command line arguments to list
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
