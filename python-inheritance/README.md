# Python - Inheritance

This repository focuses on the concept of inheritance. Inheritance is a key feature of object-oriented programming, allowing for the creation of new classes that inherit attributes and behaviors from existing ones. The repository includes Python code examples, explanations, and possibly exercises or projects.

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/LEANING_OBJECTIVES.md) file for details.

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

### 0. Lookup

**File:** [0-lookup.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/0-lookup.py)<br>
**Description:** Write a function that returns the list of available attributes and methods of an object.<br>
**Requirement:** <br>
- Prototype: def lookup(obj):
- Returns a list object
- You are not allowed to import any module

### 1. My list

**File:** [1-my_list.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/1-my_list.py)<br>
**Description:** Write a class MyList that inherits from list.<br>
**Requirement:** <br>
- Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type int
- You are not allowed to import any module

### 2. Exact same object

**File:** [2-is_same_class.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/2-is_same_class.py)<br>
**Description:** Write a function that returns True if the object is exactly an instance of the specified class, otherwise False.<br>
**Requirement:** <br>
- Prototype: def is_same_class(obj, a_class):
- You are not allowed to import any module

### 3. Same class or inherit from

**File:** [3-is_kind_of_class.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/3-is_kind_of_class.py)<br>
**Description:** Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.<br>
**Requirement:** <br>
- Prototype: def is_kind_of_class(obj, a_class):
- You are not allowed to import any module

### 4. Only sub class of

**File:** [4-inherits_from.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/4-inherits_from.py)<br>
**Description:** Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.<br>
**Requirement:** <br>
- Prototype: def inherits_from(obj, a_class):
- You are not allowed to import any module

### 5. Geometry module

**File:** [5-base_geometry.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/5-base_geometry.py)<br>
**Description:** Write an empty class BaseGeometry.<br>
**Requirement:** <br>
- You are not allowed to import any module

### 6. Improve Geometry

**File:** [6-base_geometry.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/6-base_geometry.py)<br>
**Description:** Write a class BaseGeometry (based on 5-base_geometry.py).<br>
**Requirement:** <br>
- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- You are not allowed to import any module

### 7. Integer validator

**File:** [7-base_geometry.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/7-base_geometry.py)<br>
**Description:** Write a class BaseGeometry (based on 6-base_geometry.py).<br>
**Requirement:** <br>
- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- Public instance method: def integer_validator(self, name, value): that validates value:
-- you can assume name is always a string
-- if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
-- if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
- You are not allowed to import any module

### 8. Rectangle

**File:** [8-rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/8-rectangle.py)<br>
**Description:** Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).<br>
**Requirement:** <br>
- Instantiation with width and height: def __init__(self, width, height):
-- width and height must be private. No getter or setter
-- width and height must be positive integers, validated by integer_validator


### 9. Full rectangle

**File:** [9-rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-inheritance/9-rectangle.py)<br>
**Description:** Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py).<br>
**Requirement:** <br>
- Instantiation with width and height: def __init__(self, width, height):
-- width and height must be private. No getter or setter
-- width and height must be positive integers, validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>