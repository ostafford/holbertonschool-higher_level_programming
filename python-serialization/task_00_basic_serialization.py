import json


def serialize_and_save_to_file(data: dict, filename: str) -> None:
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): The dictionary to serialize
        filename (str): The output JSON filename

    Raises:
        OSError: If there's an error writing to the file
        TypeError: If the data cannot be serialized to JSON
    """
    # No try-except here - let the exception propagate up
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


def load_and_deserialize(filename: str) -> dict:
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The input JSON filename

    Returns:
        dict: The deserialized dictionary

    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    with open(filename, 'r') as file:
        return json.load(file)
