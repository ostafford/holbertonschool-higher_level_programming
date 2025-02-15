import xml.etree.ElementTree as ET
from typing import Dict, Any


def detect_type(value: str) -> Any:
    """
    Detect and convert string value to appropriate Python type.

    Args:
        value (str): String value to convert

    Returns:
        Converted value in appropriate type
    """
    # Handle boolean
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False

    # Handle null/None
    if value.lower() == 'none' or value.lower() == 'null':
        return None

    # Handle numbers
    try:
        # Try integer first
        if value.isdigit():
            return int(value)
        # Then try float
        return float(value)
    except ValueError:
        # If not a number, return as string
        return value


def serialize_to_xml(dictionary: Dict[str, Any], filename: str) -> bool:
    """
    Serialize a Python dictionary to XML and save to file.

    Args:
        dictionary (Dict): Dictionary to serialize
        filename (str): Output filename

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create the root element
        root = ET.Element('data')

        # Add dictionary items as child elements
        for key, value in dictionary.items():
            # Create child element
            child = ET.SubElement(root, 'item')

            # Add key and value as attributes
            child.set('key', str(key))
            child.set('value', str(value))

            # Add type information
            child.set('type', type(value).__name__)

        # Create the ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True

    except Exception as e:
        print(f"Error during serialization: {str(e)}")
        return False


def deserialize_from_xml(filename: str) -> Dict[str, Any]:
    """
    Deserialize XML file back to Python dictionary.

    Args:
        filename (str): Input XML filename

    Returns:
        Dict: Deserialized dictionary or empty dict if error occurs
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Create dictionary to store results
        result = {}

        # Process each item element
        for item in root.findall('item'):
            key = item.get('key')
            value = item.get('value')
            value_type = item.get('type')

            # Convert value based on type
            if value_type == 'int':
                value = int(value)
            elif value_type == 'float':
                value = float(value)
            elif value_type == 'bool':
                value = value.lower() == 'true'
            elif value_type == 'NoneType':
                value = None

            result[key] = value

        return result

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return {}
    except ET.ParseError:
        print(f"Error parsing XML file: {filename}")
        return {}
    except Exception as e:
        print(f"Error during deserialization: {str(e)}")
        return {}


# Test the implementation
if __name__ == "__main__":
    # Test dictionary with various types
    test_dict = {
        'name': 'John Doe',
        'age': 30,
        'height': 1.75,
        'is_student': True,
        'address': None
    }

    # Test serialization
    print("Testing serialization...")
    success = serialize_to_xml(test_dict, 'test_data.xml')
    print(f"Serialization successful: {success}")

    # Test deserialization
    print("\nTesting deserialization...")
    loaded_dict = deserialize_from_xml('test_data.xml')
    print("Deserialized dictionary:")
    for key, value in loaded_dict.items():
        print(f"{key}: {value} (type: {type(value).__name__})")

    # Test error handling
    print("\nTesting error handling...")
    error_dict = deserialize_from_xml('nonexistent.xml')
    print(f"Empty dictionary returned: {error_dict == {}}")
