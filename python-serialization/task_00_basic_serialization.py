import json


def serialize_and_save_to_file(data: dict, filename: str) -> None:
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): The dictionary to serialize
        filename (str): The output JSON filename
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file: {str(e)}")


def load_and_deserialize(filename: str) -> dict:
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The input JSON filename

    Returns:
        dict: The deserialized dictionary
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return {}
    except json.JSONDecodeError:
        print(f"Error: File {filename} contains invalid JSON")
        return {}
    except Exception as e:
        print(f"Error loading data from file: {str(e)}")
        return {}


# Test the functions
if __name__ == "__main__":
    # Test data
    test_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com",
        "addresses": {
            "home": "123 Home St",
            "work": "456 Work Ave"
        },
        "hobbies": ["reading", "hiking", "photography"]
    }

    # Test serialization
    print("Testing serialization...")
    serialize_and_save_to_file(test_data, "test_data.json")

    # Test deserialization
    print("\nTesting deserialization...")
    loaded_data = load_and_deserialize("test_data.json")
    print("\nLoaded data:")
    print(json.dumps(loaded_data, indent=2))

    # Verify the data matches
    print("\nVerifying data matches original...")
    print(f"Data matches: {test_data == loaded_data}")
