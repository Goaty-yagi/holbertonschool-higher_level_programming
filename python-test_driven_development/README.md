# Python - Test-driven development

This repository serves as a comprehensive guide to Test-driven Development (TDD) in Python. It offers practical examples, best practices, and step-by-step tutorials for implementing TDD methodologies in Python projects. Covering testing frameworks, methodologies, and code samples, it equips developers with the skills to write robust, testable code while fostering a culture of quality assurance within Python development workflows.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/LEANING_OBJECTIVES.md) file for details.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.\*)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.\*)
- All your files must be executable
- The length of your files will be tested using wc

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m - doctest ./tests/\*
- All your modules should have a documentation (python3 -c 'print(**import**- ("my_module").**doc**)')
- All your functions should have a documentation (python3 -c 'print- (**import**("my_module").my_function.**doc**)')
- A documentation is not a simple word, it’s a real sentence explaining - what’s the purpose of the module, class or method (the length of it will - be verified)
- We strongly encourage you to work together on test cases, so that you - don’t miss any edge case – The Checker is checking for tests!

## Practice Exercises

### 0. Integers addition

**File:** [0-add_integer.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/0-add_integer.py)<br>
**Description:** Write a function that adds 2 integers.<br>
**Requirement:** <br>

- Prototype: def add_integer(a, b=98):
- a and b must be integers or floats, otherwise raise a TypeError exception - with the message a must be an integer or b must be an integer
- a and b must be first casted to integers if they are float
- Returns an integer: the addition of a and b
- You are not allowed to import any module

### 1. Divide a matrix

**File:** [2-matrix_divided.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/2-matrix_divided.py)<br>
**Description:** Write a function that divides all elements of a matrix<br>
**Requirement:** <br>

- Prototype: def matrix_divided(matrix, div):
- matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
- Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
- div must be a number (integer or float), otherwise raise a TypeError - exception with the message div must be a number
- div can’t be equal to 0, otherwise raise a ZeroDivisionError exception - with the message division by zero
- All elements of the matrix should be divided by div, rounded to 2 decimal - places
- Returns a new matrix
- You are not allowed to import any module

### 2. Say my name

**File:** [3-say_my_name.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/3-say_my_name.py)<br>
**Description:** Write a function that prints My name is <first name> <last name>.<br>
**Requirement:** <br>

- Prototype: def say_my_name(first_name, last_name=""):
- first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
- You are not allowed to import any module


### 3. Print square

**File:** [4-print_square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/4-print_square.py)<br>
**Description:** Write a function that prints a square with the character #.<br>
**Requirement:** <br>

- Prototype: def print_square(size):
- size is the size length of the square
- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size - must be >= 0
- if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
- You are not allowed to import any module


### 4. Text indentation

**File:** [5-text_indentation.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/5-text_indentation.py)<br>
**Description:** Write a function that prints a text with 2 new lines after each of these characters: ., ? and :.<br>
**Requirement:** <br>

- Prototype: def text_indentation(text):
- text must be a string, otherwise raise a TypeError exception with the message text must be a string
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module


### 5. Max integer - Unittest

**File:** [tests/6-max_integer_test.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/tests/6-max_integer_test.py)<br>
**Description:** Write unittests for the function def max_integer(list=[]):.<br>
**Requirement:** <br>
- Your test file should be inside a folder tests
- You have to use the unittest module
- Your test file should be python files (extension: .py)
- Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

