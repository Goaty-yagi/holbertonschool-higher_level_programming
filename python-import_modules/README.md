# Python - import & modules

This project includes a comprehensive practice to understanding and harnessing the power of Python's import system and modules.

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
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Practice Exercises

### 0. Import a simple function from a simple file

**File:** [0-add.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-import_modules/0-add.py)<br>
**Description:** Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3.<br>
**Requirement:** <br>
- You have to use print function with string format to display integers
- You have to assign:
-- the value 1 to a variable called a
-- the value 2 to a variable called b
-- and use those two variables as arguments when calling the functions add and print
- a and b must be defined in 2 different lines: a = 1 and another b = 2
- Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
- You can only use the word add_0 once in your code
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported - by using __import__, like the example below


### 1. My first toolbox!

**File:** [1-calculation.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-import_modules/1-calculation.py)<br>
**Description:** Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.<br>
**Requirement:** <br>
- Do not use the function print (with string format to display integers) more than 4 times
- You have to define:
-- the value 10 to a variable a
-- the value 5 to a variable b
-- and use those two variables only, as arguments when calling functions (including print)
- a and b must be defined in 2 different lines: a = 10 and another b = 5
- Your program should call each of the imported functions.
- the word calculator_1 should be used only once in your file
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

### 2. How to make a script dynamic!

**File:** [2-args.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-import_modules/2-args.py)<br>
**Description:** Write a program that prints the number of and the list of its arguments.<br>
**Requirement:** <br>
- The output should be:
-- Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
-- : (or . if no arguments were passed) followed by
-- a new line, followed by (if at least one argument),
-- one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of argv can be retrieved by using: len(argv)
- You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.


### 3. Infinite addition

**File:** [3-infinite_add.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-import_modules/3-infinite_add.py)<br>
**Description:** Write a program that prints the result of the addition of all arguments.<br>
**Requirement:** <br>
- The output should be the result of the addition of all arguments, followed by a new line
- You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
- Your code should not be executed when imported


### 4. Who are you?

**File:** [4-hidden_discovery.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-import_modules/4-hidden_discovery.py)<br>
**Description:** Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally in your sandbox using curl).<br>
**Requirement:** <br>
- You should print one name per line, in alpha order
- You should print only names that do not start with __
- Your code should not be executed when imported
- Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)


### 5. Everything can be imported

**File:** [5-variable_load.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-import_modules/5-variable_load.py)<br>
**Description:** Write a program that imports the variable a from the file variable_load_5.py and prints its value.<br>
**Requirement:** <br>
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported


## Tests
This project includes a comprehensive suite of tests to ensure the reliability and functionality of the codebase. These tests cover various aspects, including unit tests.<br>

### [Running Tests](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/tree/main/python-if_else_loops_functions/tests)
 There are two ways to run the tests.

- 1, Run the following command in the root dir.<br>
   `python3 <path of the test> ` ex) `python3 tests/test0.py`
- 2, Run with Makefile command.
  This project includes Makefile to automate testing processes.<br>
  `make` command run the all test files in the tests directory.<br>
  `make filename without py` such as `make test4` run the specific test file.<br>
- **Install make:** install make with `apt-get install make` (if necessary)







