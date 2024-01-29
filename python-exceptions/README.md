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

