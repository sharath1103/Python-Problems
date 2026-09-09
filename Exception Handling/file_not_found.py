filename = "missing_file.txt"

try:
    with open(filename, 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("The file has been not found in the folder")
