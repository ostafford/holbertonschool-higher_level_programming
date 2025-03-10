import json

# Serialization (Python to JSON)
python_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(python_dict)  # Convert to JSON string
with open('data.json', 'w') as file:
    json.dump(python_dict, file)

