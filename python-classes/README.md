<p align="center">
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/247/oop-meme.jpg" alt="thumbnail">
</p>

# Python - Classes and Objects

This Python repository dedicate to exploring the fundamentals and advanced concepts of object-oriented programming (OOP) in Python. It contains comprehensive examples, tutorials, and exercises covering the creation and usage of classes, inheritance, polymorphism, encapsulation, and other key OOP principles.  

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)
## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-classes/LEARNING_OBJECTIVES.md) file for details.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").- my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or - method (the length of it will be verified)

## Practice Exercises

### 0. My first square

**File:** [0-square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-classes/0-square.py)<br>
**Description:** Write an empty class Square that defines a square.<br>
**Requirement:** <br>
- You are not allowed to import any module


### 1. Square with size

**File:** [1-square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-classes/1-square.py)<br>
**Description:** Write a class Square that defines a square by: (based on 0-square.py).<br>
**Requirement:** <br>
- Private instance attribute: size
- Instantiation with size (no type/value verification)
- You are not allowed to import any module

### 2. Size validation

**File:** [2-square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-classes/2-square.py)<br>
**Description:** Write a class Square that defines a square by: (based on 1-square.py).<br>
**Requirement:** <br>
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
-- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
-- if size is less than 0, raise a ValueError exception with the message size - must be >= 0
- You are not allowed to import any module

### 3. Area of a square

**File:** [3-square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-classes/3-square.py)<br>
**Description:** Write a class Square that defines a square by: (based on 2-square.py).<br>
**Requirement:** <br>
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
--  size must be an integer, otherwise raise a TypeError exception with the - message size must be an integer
--  if size is less than 0, raise a ValueError exception with the message size - must be >= 0
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module

### 4. Access and update private attribute

**File:** [4-square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-classes/4-square.py)<br>
**Description:** Write a class Square that defines a square by: (based on 3-square.py).<br>
**Requirement:** <br>
- Private instance attribute: size:
-- property def size(self): to retrieve it
-- property setter def size(self, value): to set it:
--- size must be an integer, otherwise raise a TypeError exception with the - message size must be an integer
--- if size is less than 0, raise a ValueError exception with the message size - must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module


### 5. Printing a square

**File:** [5-square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-classes/5-square.py)<br>
**Description:** Write a class Square that defines a square by: (based on 4-square.py).<br>
**Requirement:** <br>
- Private instance attribute: size:
-- property def size(self): to retrieve it
-- property setter def size(self, value): to set it:
--- size must be an integer, otherwise raise a TypeError exception with the - message size must be an integer
--- if size is less than 0, raise a ValueError exception with the message size - must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
-- if size is equal to 0, print an empty line
- You are not allowed to import any module


### 6. Coordinates of a square

**File:** [6-square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-classes/6-square.py)<br>
**Description:** Write a class Square that defines a square by: (based on 5-square.py).<br>
**Requirement:** <br>
- Private instance attribute: size:
-- property def size(self): to retrieve it
-- property setter def size(self, value): to set it:
--- size must be an integer, otherwise raise a TypeError exception with the - message size must be an integer
--- if size is less than 0, raise a ValueError exception with the message size - must be >= 0
- Private instance attribute: position:
-- property def position(self): to retrieve it
-- property setter def position(self, value): to set it:
--- position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
- Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
-- if size is equal to 0, print an empty line
-- position should be use by using space - Don’t fill lines by spaces when position[1] > 0
- You are not allowed to import any module

