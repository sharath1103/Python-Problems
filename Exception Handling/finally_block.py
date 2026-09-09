def read_file(filename):
    f = None
    try:
        f = open(filename, "r")
        content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: '{filename}' not found."
    finally:
        if f:
            f.close()
        print("File closed.")

print(read_file("hello.txt"))
print("---")
print(read_file("missing.txt"))