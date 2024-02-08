# Learning Objectives

- [How to open a file](#how-to-open-a-file)
- [How to write text in a file](#how-to-write-text-in-a-file)
- [How to read the full content of a file](#how-to-read-the-full-content-of-a-file)
- [How to read a file line by line](#how-to-read-a-file-line-by-line)
- [How to move the cursor in a file](#how-to-move-the-cursor-in-a-file)
- [How to make sure a file is closed after using it](#how-to-make-sure-a-file-is-closed-after-using-it)
- [What is and how to use the with statement](#what-is-and-how-to-use-the-with-statement)
- [What is JSON](#what-is-JSON)
- [What is serialization](#what-is-serialization)
- [What is deserialization](#what-is-deserialization)
- [How to convert a Python data structure to a JSON string](#how-to-convert-a-Python-data-structure-to-a-JSON-string)
- [How to convert a JSON string to a Python data structure](#how-to-convert-a-JSON-string-to-a-Python-data-structure)
- [How to access command line parameters in a Python script](#how-to-access-command-line-parameters-in-a-Python-script)

## How to open a file
You can open a file using the open() function, which returns a file object. 
```python
file = open('filename', 'mode')

file.close() # don't forget to close

```
Here are some common modes:

'r': Read (default). Opens the file for reading.
'w': Write. Opens the file for writing. Creates a new file or truncates an existing file to zero length.
'a': Append. Opens the file for writing at the end of the file. Creates a new file if it does not exist.
'b': Binary mode. Opens the file in binary mode.
'+': Open for updating (reading and writing)
```python
# Open a file named 'example.txt' for reading
with open('example.txt', 'r') as file:
    # Perform operations on the file
    content = file.read()
    print(content)

```
Make sure to use the with statement when opening a file. It ensures that the file is properly closed after you're done with it, even if an exception occurs during the operations inside the with block.
## How to write text in a file
You can use 'w' or 'a' as the mode, respectively. Remember to handle exceptions, such as FileNotFoundError if the file doesn't exist.
```python
# Open a file named 'output.txt' for writing
with open('output.txt', 'w') as file:
    file.write('Hello, World!')

```
## How to read the full content of a file
You can use read method to read full file.

```python
with open('example.txt', 'r') as file:
    # Read the full content of the file
    content = file.read()
    print(content)
```
## How to read a file line by line
You can use readlines method to read line by line.

```python
with open('example.txt', 'r') as file:
    # Read the full content of the file line by line
    lines = file.readlines() # return list
    print(lines)
```
## How to move the cursor in a file
You can move the cursor position in a file using the seek() method.
- offset: The number of bytes to move the cursor. A positive value moves the cursor forward, and a negative value moves it backward.
- whence: The reference point for the offset. It can take one of the following values:
0 (default): Start of the file
1: Current position
2: End of the file

```python
# Open the file in binary read mode
with open('example.txt', 'rb') as file:
    # Read and print the content before moving the cursor
    content_before = file.read()
    print("Content before:", content_before)

    # Move the cursor one byte forward from the beginning of the file (offset=1, whence=0)
    file.seek(1, 0)

    # Read and print the content after moving the cursor
    content_after = file.read()
    print("Content after:", content_after)

```
## How to make sure a file is closed after using it
You can use close method, or with statement to open the file.
```python
# Open the file
file = open('example.txt', 'r')

try:
    # Perform operations on the file
    content = file.read()
    print(content)
finally:
    # Ensure the file is closed, even if an exception is raised
    file.close()

```
## What is and how to use the with statement
The with statement in Python is used to simplify the management of resources, such as files, network connections, or database connections, by ensuring that certain operations are properly handled, and resources are correctly managed.
```python
# Using 'with' statement to open and automatically close the file
with open('example.txt', 'r') as file:
    # Code block to perform operations on the file
    content = file.read()
    print(content)

# The file is automatically closed when the 'with' block is exited

```
## What is JSON
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is a text-based data format that represents structured data in a key-value pair format.

- Data Structure: JSON supports data types such as objects (unordered collections of key-value pairs), arrays (ordered lists of values), strings, numbers, booleans, and null.

- Human-Readable: JSON data is easy for humans to read and write. It uses a syntax similar to JavaScript object literal notation, making it familiar to developers in various programming languages.

- Language Agnostic: While inspired by JavaScript, JSON is language-agnostic and widely used with many programming languages, not just JavaScript.

- Data Exchange: JSON is commonly used for data exchange between a server and a web application, as well as for configuration files and other data storage scenarios.

```json
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "isStudent": false,
  "grades": [95, 87, 92],
  "address": {
    "street": "123 Main St",
    "zipCode": "10001"
  }
}
```
Python has a built-in module called json that provides methods for encoding and decoding JSON data. For example, json.dumps() is used to serialize a Python object into a JSON-formatted string, and json.loads() is used to deserialize a JSON-formatted string into a Python object.
## What is serialization
Serialization is the process of converting a data structure or object into a format that can be easily stored or transmitted and later reconstructed.
json.dumps() is used to serialize a Python object into a JSON-formatted string
## What is deserialization
Deserialization is the process of reconstructing a data structure or object from a serialized format. 
json.loads() is used to deserialize a JSON-formatted string into a Python object.
## How to convert a Python data structure to a JSON string
You can use json module to serialize a Python object into a JSON-formatted string

- json.dumps : This function is used to serialize a Python object to a JSON-formatted string.
```python
import json

# Python data structure (a dictionary in this case)
python_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False
}

# Convert Python data structure to a JSON string
json_string = json.dumps(python_data)

# Print the JSON string
print(json_string)

```

- json.dump(): This function is used to write Python data structure to the file as a JSON-formatted string
```python
import json

# Python data structure (a dictionary in this case)
python_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False
}

# Open a file for writing
with open('output.json', 'w') as json_file:
    # Write Python data structure to the file as a JSON-formatted string
    json.dump(python_data, json_file)

```
## How to convert a JSON string to a Python data structure
You can convert a JSON string to a Python data structure using the json module. 

- json.loads(): This function is used to deserialize a JSON-formatted string to a Python object.
```python
import json

# JSON-formatted string
json_string = '{"name": "John Doe", "age": 30, "city": "New York", "is_student": false}'

# Convert JSON string to a Python data structure
python_data = json.loads(json_string)

# Print the Python data structure
print(python_data)

```

- json.load(): This function is used to read a JSON-formatted string from a file-like object and convert it to a Python object.

```python
import json

# Open a file for reading
with open('input.json', 'r') as json_file:
    # Read the JSON-formatted string from the file and convert it to a Python data structure
    python_data = json.load(json_file)

# Print the Python data structure
print(python_data)

```
## How to access command line parameters in a Python script
In Python, you can access command line parameters using the sys module.

```python
import sys

# Check the number of command-line arguments
num_args = len(sys.argv)

# Print the script name (first element in sys.argv)
print(f"Script name: {sys.argv[0]}")

# Print the command-line arguments (starting from the second element)
print("Command-line arguments:")
for arg in sys.argv[1:]:
    print(arg)

```
