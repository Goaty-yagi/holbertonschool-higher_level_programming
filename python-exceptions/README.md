# Python - Exceptions

This repository provides examples and explanations for handling exceptions in Python. Learn how to effectively use try-except blocks, raise custom exceptions, and manage errors gracefully in Python programs.

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/LEANING_OBJECTIVES.md) file for details.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Practice Exercises

### 0. Safe list printing

**File:** [0-safe_print_list.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/0-safe_print_list.py)<br>
**Description:** Write a function that prints x elements of a list.<br>
**Requirement:** <br>
- Prototype: def safe_print_list(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- x represents the number of elements to print
- x can be bigger than the length of my_list
- Returns the real number of elements printed
- You have to use try: / except:
- You are not allowed to import any module
- You are not allowed to use len()


### 1. Safe printing of an integers list

**File:** [1-safe_print_integer.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/1-safe_print_integer.py)<br>
**Description:** Write a function that prints an integer with "{:d}".format().<br>
**Requirement:** <br>
- Prototype: def safe_print_integer(value):
- value can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns True if value has been correctly printed (it means the value is an integer)
- Otherwise, returns False
- You have to use try: / except:
- You have to use "{:d}".format() to print as integer
- You are not allowed to import any module
- You are not allowed to use type()

### 2. Print and count integers

**File:** [2-safe_print_list_integers.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/2-safe_print_list_integers.py)<br>
**Description:** Write a function that prints the first x elements of a list and only integers.<br>
**Requirement:** <br>
- Prototype: def safe_print_list_integers(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- You have to use try: / except:
- You have to use "{:d}".format() to print an integer
- You are not allowed to import any module
- You are not allowed to use len()

### 3. Integers division with debug

**File:** [3-safe_print_division.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/3-safe_print_division.py)<br>
**Description:** Write a function that divides 2 integers and prints the result.<br>
**Requirement:** <br>
- Prototype: def safe_print_division(a, b):
- You can assume that a and b are integers
- The result of the division should print on the finally: section preceded by Inside result:
- Returns the value of the division, otherwise: None
- You have to use try: / except: / finally:
- You have to use "{}".format() to print the result
- You are not allowed to import any module


### 4. Divide a list

**File:** [4-list_division.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/4-list_division.py)<br>
**Description:** Write a function that divides element by element 2 lists.<br>
**Requirement:** <br>
- Prototype: def list_division(my_list_1, my_list_2, list_length):
- my_list_1 and my_list_2 can contain any type (integer, string, etc.)
- list_length can be bigger than the length of both lists
- Returns a new list (length = list_length) with all divisions
- If 2 elements can’t be divided, the division result should be equal to 0
- If an element is not an integer or float:
print: wrong type
- If the division can’t be done (/0):
print: division by 0
- If my_list_1 or my_list_2 is too short
print: out of range
- You have to use try: / except: / finally:
- You are not allowed to import any module


### 5. Raise exception

**File:** [5-raise_exception.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/5-raise_exception.py)<br>
**Description:** Write a function that raises a type exception.<br>
**Requirement:** <br>
- Prototype: def raise_exception():
- You are not allowed to import any module