# Python - Data Structures: Lists, Tuples

This repository contains Python code examples and explanations for working with two fundamental data structures: Lists and Tuples. Whether you're a beginner learning Python or an experienced developer looking for a quick reference, this repository aims to provide clear and concise examples to enhance your understanding.

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

### 0. Print a list of integers

**File:** `0-print_list_integer.py`
**Description:** Write a function that prints all integers of a list.
**Requirement:** 
- Prototype: def print_list_integer(my_list=[]):
- Format: one integer per line.
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers

### 1. Secure access to an element in a list

**File:** `1-element_at.py`
**Description:** Write a function that retrieves an element from a list.
**Requirement:** 
- Prototype: def element_at(my_list, idx):
- If idx is negative, the function should return None
- If idx is out of range (> of number of element in my_list), the function should return None
- You are not allowed to import any module
- You are not allowed to use try/except


### 2. Replace element

**File:** `2-replace_in_list.py`
**Description:** Write a function that replaces an element of a list at a specific position.
**Requirement:** 
- Prototype: def replace_in_list(my_list, idx, element):
- If idx is negative, the function should not modify anything, and returns the original list
- If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use try/except

