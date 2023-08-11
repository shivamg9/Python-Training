"""
Write a program to handle file open/close and read/write functionality using Exception handling

"""


def read_file(filename):
    try:
        _file = open(filename, "r")
        content = _file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied to open file '{filename}'.")
    finally:
        if "file" in locals():
            _file.close()


def write_file(filename, content):
    try:
        _file = open(filename, "w")
        _file.write(content)
        print(f"Content successfully written to file '{filename}'.")
    except PermissionError:
        print(f"Permission denied to write to file '{filename}'.")
    finally:
        if "file" in locals():
            _file.close()


# Example usage:
read_file("example.txt")
write_file("example.txt", "This is an example. It adds file as named 'example'.")
read_file("example.txt")
