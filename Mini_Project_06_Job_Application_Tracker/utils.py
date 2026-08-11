import json
import os

def initialize_file(filename):
    """
    Create a JSON file if it does not already exist.

    Parameters:
    - filename (str): Name of the JSON file.
    """
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file, indent=4)

def read_json(filename):
    """
    Read and return data from a JSON file.

    Parameters:
    - filename (str): Name of the JSON file.

    Returns:
    - list: Data stored in the JSON file.
    """
    initialize_file(filename)

    with open(filename, "r") as file:
        return json.load(file)

def write_json(filename, data):
    """
    Write data to a JSON file.

    Parameters:
    - filename (str): Name of the JSON file.
    - data (list): Data to write into the file.
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)