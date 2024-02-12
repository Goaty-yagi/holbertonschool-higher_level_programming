<p align="center">
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/331/giphy.mp4" alt="thumbnail">
</p>

# Python - Almost a circle

This is a versatile repository that not only generates an approximation of a circle but also serves as an educational hub for various Python topics. Explore unit testing implementation in large projects, learn the ins and outs of serializing and deserializing classes, master the art of working with JSON files, and delve into the power of \*args, \*\*kwargs, and named arguments in functions.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/LEARNING_OBJECTIVES.md) file for details.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.\*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should be documented: python3 -c 'print(**import**("my_module").**doc**)'
- All your classes should be documented: python3 -c 'print(**import**("my_module").MyClass.**doc**)'
- All your functions (inside and outside a class) should be documented: python3 -c 'print(**import**("my_module").my_function.**doc**)' and python3 -c 'print(**import**("my_module").MyClass.my_function.**doc**)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start with test\_
- Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
- We strongly encourage you to work together on test cases so that you don’t miss any edge case

## Practice Exercises

### 1. Base class

**File:** [models/base.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/base.py)<br>
**Description:** Create a folder named models with an empty file **init**.py inside - with this file, the folder will become a Python package.<br>
**Requirement:** <br>

- Class Base:
  -- private class attribute **nb_objects = 0
  -- class constructor: def **init**(self, id=None)::
  --- if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
  --- otherwise, increment **nb_objects and assign the new value to the public instance attribute id

### 2. First Rectangle

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Write the class Rectangle that inherits from Base.<br>
**Requirement:** <br>

- In the file models/rectangle.py
- Class Rectangle inherits from Base
- Private instance attributes, each with its own public getter and setter:
  -- **width -> width
  -- **height -> height
  -- **x -> x
  -- **y -> y
- Class constructor: def **init**(self, width, height, x=0, y=0, id=None):
  -- Call the super class with id - this super call with use the logic of the **init** of the Base class
  -- Assign each argument width, height, x and y to the right attribute

### 3. Validate attributes

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).<br>
**Requirement:** <br>

- If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
- If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
- If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0

### 4. Area first

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.<br>
