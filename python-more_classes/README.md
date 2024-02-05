<p align="center">
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/247/oop-meme.jpg" alt="thumbnail">
</p>

# Python - More Classes and Objects

This repository delves into advanced concepts related to classes and objects in Python, building upon the fundamentals of object-oriented programming (OOP). Explore these topics to enhance your understanding and proficiency in designing robust and flexible software using Python.

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_classes/LEANING_OBJECTIVES.md) file for details.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Practice Exercises

### 0. Simple rectangle

**File:** [0-rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_classes/0-rectangle.py)<br>
**Description:** Write an empty class Rectangle that defines a rectangle.<br>
**Requirement:** <br>
- You are not allowed to import any module

### 1. Real definition of a rectangle

**File:** [1-rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_classes/1-rectangle.py)<br>
**Description:** Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py).<br>
**Requirement:** <br>
- Private instance attribute: width:
-- property def width(self): to retrieve it
-- property setter def width(self, value): to set it:
--- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
--- if width is less than 0, raise a ValueError exception with the message width must be >= 0
- Private instance attribute: height:
-- property def height(self): to retrieve it
-- property setter def height(self, value): to set it:
--- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
--- if height is less than 0, raise a ValueError exception with the message height must be >= 0
- Instantiation with optional width and height: def __init__(self, width=0, height=0):
- You are not allowed to import any module


### 2. Area and Perimeter

**File:** [2-rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_classes/2-rectangle.py)<br>
**Description:** Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py).<br>
**Requirement:** <br>
- Private instance attribute: width:
-- property def width(self): to retrieve it
-- property setter def width(self, value): to set it:
--- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
--- if width is less than 0, raise a ValueError exception with the message width must be >= 0
- Private instance attribute: height:
-- property def height(self): to retrieve it
-- property setter def height(self, value): to set it:
--- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
--- if height is less than 0, raise a ValueError exception with the message height must be >= 0
- Instantiation with optional width and height: def __init__(self, width=0, height=0):
- Public instance method: def area(self): that returns the rectangle area
- Public instance method: def perimeter(self): that returns the rectangle perimeter:
-- if width or height is equal to 0, perimeter is equal to 0
- You are not allowed to import any module

### 3. String representation

**File:** [3-rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_classes/3-rectangle.py)<br>
**Description:** Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py).<br>
**Requirement:** <br>
- Private instance attribute: width:
-- property def width(self): to retrieve it
-- property setter def width(self, value): to set it:
--- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
--- if width is less than 0, raise a ValueError exception with the message width must be >= 0
- Private instance attribute: height:
-- property def height(self): to retrieve it
-- property setter def height(self, value): to set it:
--- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
--- if height is less than 0, raise a ValueError exception with the message height must be >= 0
- Instantiation with optional width and height: def __init__(self, width=0, height=0):
- Public instance method: def area(self): that returns the rectangle area
- Public instance method: def perimeter(self): that returns the rectangle perimeter:
-- if width or height is equal to 0, perimeter is equal to 0
- print() and str() should print the rectangle with the character #: (see example below)
-- if width or height is equal to 0, return an empty string
- You are not allowed to import any module
```bash
Area: 8 - Perimeter: 12
##
##
##
##
```

### 4. Eval is magic

**File:** [4-rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_classes/4-rectangle.py)<br>
**Description:** Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py).<br>
**Requirement:** <br>
- Private instance attribute: width:
-- property def width(self): to retrieve it
-- property setter def width(self, value): to set it:
--- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
--- if width is less than 0, raise a ValueError exception with the message width must be >= 0
- Private instance attribute: height:
-- property def height(self): to retrieve it
-- property setter def height(self, value): to set it:
--- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
--- if height is less than 0, raise a ValueError exception with the message height must be >= 0
- Instantiation with optional width and height: def __init__(self, width=0, height=0):
- Public instance method: def area(self): that returns the rectangle area
- Public instance method: def perimeter(self): that returns the rectangle perimeter:
-- if width or height is equal to 0, perimeter is equal to 0
- print() and str() should print the rectangle with the character #: (see example below)
-- if width or height is equal to 0, return an empty string
- repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
- You are not allowed to import any module
```bash
Area: 8 - Perimeter: 12
##
##
##
##
```