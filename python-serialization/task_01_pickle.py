import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize a CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in the specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str) -> bool:
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save to

        Returns:
            bool: True if successful, False if an error occurred
        """
        try:
            with open(filename, 'wb') as file:  # 'wb' for write binary
                pickle.dump(self, file)
            return True
        except Exception as e:
            print(f"Error during serialization: {str(e)}")
            return False

    @classmethod
    def deserialize(cls, filename: str) -> 'CustomObject':
        """
        Deserialize and return a CustomObject instance from a file.

        Args:
            filename (str): The name of the file to load from

        Returns:
            CustomObject or None:
            The deserialized object, or None if an error occurred
        """
        try:
            with open(filename, 'rb') as file:  # 'rb' for read binary
                return pickle.load(file)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return None
        except Exception as e:
            print(f"Error during deserialization: {str(e)}")
            return None


# Test the implementation
if __name__ == "__main__":
    # Create a test object
    test_obj = CustomObject("John", 25, True)

    # Display original object
    print("Original object:")
    test_obj.display()

    # Test serialization
    if test_obj.serialize("test_object.pickle"):
        print("\nObject successfully serialized")

    # Test deserialization
    loaded_obj = CustomObject.deserialize("test_object.pickle")
    if loaded_obj:
        print("\nDeserialized object:")
        loaded_obj.display()

    # Test error handling with non-existent file
    print("\nTrying to deserialize non-existent file:")
    result = CustomObject.deserialize("nonexistent.pickle")
    print(f"Result is None: {result is None}")
