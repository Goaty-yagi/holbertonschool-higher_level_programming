# python-hello,world

This project contains Python practice exercises related to print, index, and slicing.

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

### 0. Hello, print

**File:** `2-print.py`
**Description:** Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
**Requirement:** 
-Use the function print

### 1. Print integer

**File:** `3-print_number.py`
**Description**: Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
**Requirement:**
- You can find the source
  ```python
     #!/usr/bin/python3
     number = 98
     # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
  ```
- The output of the script should be:
  -- the number, followed by Battery street,
  -- followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings tips
### 2. Print float

**File:** `4-print_float.py`
**Description:** Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
**Requirement:** 
- You can find the source
  ```python
     #!/usr/bin/python3
     number = 3.14159
     # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
  ```
- The output of the script should be:
  -- Float:, followed by the float with only 2 digits
  -- followed by a new line
- You are not allowed to cast the variable number into a string
- You have to use f-strings tips

### 3. Print string

**File:** `5-print_string.py`
**Description:** Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
**Requirement:** 
- You can find the source
  ```python
     #!/usr/bin/python3
     str = "Holberton School"
     # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
  ```
- The output of the script should be:
  -- 3 times the value of str
  -- followed by a new line
  -- followed by the 9 first characters of str
  -- followed by a new line
- You are not allowed to cast the variable number into a string
- You have to use f-strings tips

### 4. Play with strings

**File:** `6-concat.py`
**Description:** Complete this source code to print Welcome to Holberton School!
**Requirement:** 
- You can find the source
  ```python
     #!/usr/bin/python3
     str1 = "Holberton"
     str2 = "School"
     # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
     print(f"Welcome to {str1}!")
  ```
- You are not allowed to use any loops or conditional statements.
- You have to use the variables str1 and str2 in your new line of code
- Your program should be exactly 5 lines long

### 5. Copy - Cut - Paste

**File:** `7-edges.py`
**Description:** Complete this source code
**Requirement:** 
- You can find the source
  ```python
     #!/usr/bin/python3
     word = "Holberton"
     # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
     print(f"First 3 letters: {word_first_3}")
     print(f"Last 2 letters: {word_last_2}")
     print(f"Middle word: {middle_word}")
  ```
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters


### 6. Create a new sentence

**File:** `8-concat_edges.py`
**Description:** Complete this source code to print object-oriented programming with Python, followed by a new line.
**Requirement:** 
- You can find the source
  ```python
    #!/usr/bin/python3
    str = "Python is an interpreted, interactive, object-oriented programming\
    language that combines remarkable power with very clear syntax"
  　# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
  　print(str)
  ```
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

### 7. Easter Egg

**File:** `9-easter_egg.py`
**Description:** Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
**Requirement:** 
- Your script should be maximum 98 characters long