import csv
import json


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Convert CSV file to JSON and save it as data.json

    Args:
        csv_filename (str): Name of the CSV file to convert

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV and convert to list of dictionaries
        with open(csv_filename, 'r') as csv_file:
            # Create CSV reader object
            csv_reader = csv.DictReader(csv_file)
            # Convert CSV rows to list of dictionaries
            data = list(csv_reader)

        # Write to JSON file
        with open('data.json', 'w') as json_file:
            # Convert to JSON and write to file
            json.dump(data, json_file, indent=2)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found")
        return False
    except csv.Error as e:
        print(f"Error reading CSV file: {str(e)}")
        return False
    except json.JSONDecodeError as e:
        print(f"Error creating JSON: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False


# Test the function
if __name__ == "__main__":
    # Test with a sample CSV file
    test_result = convert_csv_to_json("sample.csv")
    print(f"Conversion successful: {test_result}")

    # Test with non-existent file
    test_result = convert_csv_to_json("nonexistent.csv")
    print(f"Conversion successful: {test_result}")
