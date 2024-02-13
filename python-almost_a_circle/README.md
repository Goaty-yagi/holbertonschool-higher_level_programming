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

### 0. If it's not tested it doesn't work

**File:** [tests/](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/tests)<br>
**Description:** All your files, classes and methods must be unit tested and be PEP 8 validated.<br>

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

### 5. Display #0

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.<br>

### 6. **str**

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Update the class Rectangle by overriding the **str** method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.<br>

### 7. Display #1

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.<br>

### 8. Update #0

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Update the class Rectangle by adding the public method def update(self, \*args): that assigns an argument to each attribute.<br>
**Requirement:** <br>

- 1st argument should be the id attribute
- 2nd argument should be the width attribute
- 3rd argument should be the height attribute
- 4th argument should be the x attribute
- 5th argument should be the y attribute

### 9. Update #1

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.<br>
**Requirement:\*\* <br>

- **kwargs can be thought of as a double pointer to a dictionary: key/value
  -- As Python doesn’t have pointers, **kwargs is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
  -- \**kwargs must be skipped if *args exists and is not empty
  -- Each key in this dictionary represents an attribute to the instance

### 10. And now, the Square!

**File:** [models/square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/square.py)<br>
**Description:** Write the class Square that inherits from Rectangle.<br>
**Requirement:** <br>

- In the file models/square.py
- Class Square inherits from Rectangle
- Class constructor: def **init**(self, size, x=0, y=0, id=None)::
  -- Call the super class with id, x, y, width and height - this super call will use the logic of the **init** of the Rectangle class. The width and height must be assigned to the value of size
  -- You must not create new attributes for this class, use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height
  -- All width, height, x and y validation must inherit from Rectangle - same behavior in case of wrong data
- The overloading **str** method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height

### 11. Square size

**File:** [models/square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/square.py)<br>
**Description:** Update the class Square by adding the public getter and setter size.<br>
**Requirement:** <br>

- The setter should assign (in this order) the width and the height - with the same value
- The setter should have the same value validation as the Rectangle for width and height - No need to change the exception error message (It should be the one from width)

### 12. Square update

**File:** [models/square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/square.py)<br>
**Description:** Update the class Square by adding the public method def update(self, \*args, **kwargs) that assigns attributes.<br>
**Requirement:\*\* <br>

- \*args is the list of arguments - no-keyworded arguments
  -- 1st argument should be the id attribute
  -- 2nd argument should be the size attribute
  -- 3rd argument should be the x attribute
  -- 4th argument should be the y attribute
- \*\*kwargs can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
- \**kwargs must be skipped if *args exists and is not empty
- Each key in this dictionary represents an attribute to the instance

### 13. Rectangle instance to dictionary representation

**File:** [models/rectangle.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/rectangle.py)<br>
**Description:** Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle, This dictionary must contain.<br>
**Requirement:** <br>

- Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:
- This dictionary must contain:

-- id
-- width
-- height
-- x
-- y

### 14. Square instance to dictionary representation

**File:** [models/square.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/square.py)<br>
**Description:** Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:<br>
**Requirement:** <br>
This dictionary must contain:

- id
- size
- x
- y

### 15. Dictionary to JSON string

**File:** [models/base.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/base.py)<br>
**Description:** Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:<br>
**Requirement:** <br>

- ist_dictionaries is a list of dictionaries
- f list_dictionaries is None or empty, return the string: "[]"
- therwise, return the JSON string representation of list_dictionaries

### 16. JSON string to file

**File:** [models/base.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/base.py)<br>
**Description:** Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:<br>
**Requirement:** <br>

- list_objs is a list of instances who inherits of Base - example: list of Rectangle or list of Square instances
- If list_objs is None, save an empty list
- The filename must be: <Class name>.json - example: Rectangle.json
- You must use the static method to_json_string (created before)
- You must overwrite the file if it already exists

### 17. JSON string to dictionary

**File:** [models/base.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/base.py)<br>
**Description:** Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:<br>
**Requirement:** <br>

- son_string is a string representing a list of dictionaries
- f json_string is None or empty, return an empty list
- therwise, return the list represented by json_string

### 18. Dictionary to Instance

**File:** [models/base.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/base.py)<br>
**Description:** Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:<br>
**Requirement:\*\* <br>

- \*\*dictionary can be thought of as a double pointer to a dictionary
- To use the update method to assign all attributes, you must create a “dummy” instance before:
  Create a Rectangle or Square instance with “dummy” mandatory attributes (width, height, size, etc.)
  Call update instance method to this “dummy” instance to apply your real values
- You must use the method def update(self, \*args, \*\*kwargs)
- **dictionary must be used as **kwargs of the method update
- You are not allowed to use eval

### 19. File to instances

**File:** [models/base.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/base.py)<br>
**Description:** Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:<br>
**Requirement:** <br>

- The filename must be: <Class name>.json - example: Rectangle.json
- If the file doesn’t exist, return an empty list
- Otherwise, return a list of instances - the type of these instances depends on cls (current class using this method)
- You must use the from_json_string and create methods (implemented previously)


### 20. Let's draw it

**File:** [models/base.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-almost_a_circle/models/base.py)<br>
**Description:** Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:<br>
**Requirement:** <br>

- You must use the Turtle graphics module
- To install it: sudo apt-get install python3-tk
- To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: config.ssh.forward_x11 = true
- No constraints for color, shape etc… be creative!
