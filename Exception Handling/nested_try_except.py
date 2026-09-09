import json

def load_and_parse(filename, key):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        try:
            value = data[key]
            print(value)
        except KeyError:
            print(f"Error: key '{key}' not found in the data.")
    except FileNotFoundError:
        print(f"Error: file '{filename}' does not exist.")

load_and_parse("data.json", "name") 