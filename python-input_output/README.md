# Python - Input/Output

A Python Input/Output project typically involves creating a program that interacts with external data or users through various input and output mechanisms. This can include reading from and writing to files, receiving input from users through the console, handling command-line arguments, and more.

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/LEARNING_OBJECTIVES.md) file for details.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Python Test Case
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Practice Exercises

### 0. Read file

**File:** [0-read_file.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/0-read_file.py)<br>
**Description:** Write a function that reads a text file (UTF8) and prints it to stdout.<br>
**Requirement:** <br>
- Prototype: def read_file(filename=""):
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module


### 1. Write to a file

**File:** [1-write_file.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/1-write_file.py)<br>
**Description:** Write a function that writes a string to a text file (UTF8) and returns the number of characters written.<br>
**Requirement:** <br>
- Prototype: def write_file(filename="", text=""):
- You must use the with statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module


### 2. Append to a file

**File:** [2-append_write.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/2-append_write.py)<br>
**Description:** Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.<br>
**Requirement:** <br>
- Prototype: def append_write(filename="", text=""):
- If the file doesn’t exist, it should be created
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

### 3. To JSON string

**File:** [3-to_json_string.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/3-to_json_string.py)<br>
**Description:** Write a function that returns the JSON representation of an object (string).<br>
**Requirement:** <br>
- Prototype: def to_json_string(my_obj):
- You don’t need to manage exceptions if the object can’t be serialized.


### 4. From JSON string to Object

**File:** [4-from_json_string.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/4-from_json_string.py)<br>
**Description:** Write a function that returns an object (Python data structure) represented by a JSON string.<br>
**Requirement:** <br>
- Prototype: def from_json_string(my_str):
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.


### 5. Save Object to a file

**File:** [5-save_to_json_file.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/5-save_to_json_file.py)<br>
**Description:** Write a function that writes an Object to a text file, using a JSON representation.<br>
**Requirement:** <br>
- Prototype: def save_to_json_file(my_obj, filename):
- You must use the with statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.


### 6. Create object from a JSON file

**File:** [6-load_from_json_file.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/6-load_from_json_file.py)<br>
**Description:** Write a function that creates an Object from a “JSON file”.<br>
**Requirement:** <br>
- Prototype: def load_from_json_file(filename):
- You must use the with statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.


### 7. Load, add, save

**File:** [7-add_item.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/7-add_item.py)<br>
**Description:** Write a script that adds all arguments to a Python list, and then save them to a file.<br>
**Requirement:** <br>
- You must use your function save_to_json_file from 5-save_to_json_file.py
- You must use your function load_from_json_file from 6-load_from_json_file.py
- The list must be saved as a JSON representation in a file named add_item.json
- If the file doesn’t exist, it should be created
- You don’t need to manage file permissions / exceptions.


### 8. Class to JSON

**File:** [8-class_to_json.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/8-class_to_json.py)<br>
**Description:** Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.<br>
**Requirement:** <br>
- Prototype: def class_to_json(obj):
- obj is an instance of a Class
- All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module


### 9. Student to JSON

**File:** [9-student.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/9-student.py)<br>
**Description:** Write a class Student that defines a student by:<br>
**Requirement:** <br>
- Public instance attributes:
 `first_name`
 `last_name`
 `age`
- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
- Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
- You are not allowed to import any module

### 10. Student to JSON with filter

**File:** [10-student.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/10-student.py)<br>
**Description:** Write a class Student that defines a student by: (based on 9-student.py)<br>
**Requirement:** <br>
- Public instance attributes:
 `first_name`
 `last_name`
 `age`
- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
-- If attrs is a list of strings, only attribute names contained in this list must be retrieved.
-- Otherwise, all attributes must be retrieved
- You are not allowed to import any module


### 11. Student to disk and reload

**File:** [11-student.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/11-student.py)<br>
**Description:** Write a class Student that defines a student by: (based on 10-student.py)<br>
**Requirement:** <br>
- Public instance attributes:
 `first_name`
 `last_name`
 `age`
- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
-- If attrs is a list of strings, only attribute names contained in this list must be retrieved.
-- Otherwise, all attributes must be retrieved
- Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
-- You can assume json will always be a dictionary
-- A dictionary key will be the public attribute name
-- A dictionary value will be the value of the public attribute
- You are not allowed to import any module


### 12. Pascal's Triangle

**File:** [12-pascal_triangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-input_output/12-pascal_triangle.py)<br>
**Description:** Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n.<br>
**Requirement:** <br>
- Returns an empty list if n <= 0
- You can assume n will be always an integer
- You are not allowed to import any module