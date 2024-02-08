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

