# Python - Object-Relational Mapping
This project serves as a comprehensive guide and demonstration of using ORM frameworks in Python for interacting with relational databases.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Your files will be executed with MySQLdb version 2.0.x
- Your files will be executed with SQLAlchemy version 1.4.x
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use execute with sqlalchemy


## Practice Exercises

### 0. Get all states

**File:** [0-select_states.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/0-select_states.py)<br>
**Description:** Write a script that lists all states from the database hbtn_0e_0_usa<br>
**Requirement:** <br>
- Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

### 1. Filter states

**File:** [1-filter_states.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/1-filter_states.py)<br>
**Description:** Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa<br>
**Requirement:** <br>
- Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported


### 2. Filter states by user input

**File:** [2-my_filter_states.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/2-my_filter_states.py)<br>
**Description:** Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.<br>
**Requirement:** <br>
- Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- You must use format to create the SQL query with the user input
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported


### 3. SQL Injection...
Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
```bash
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/$ 
```

What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

**File:** [3-my_safe_filter_states.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/3-my_safe_filter_states.py)<br>
**Description:** write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!<br>
**Requirement:** <br>
- Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

### 4. Cities by states

**File:** [4-cities_by_state.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/4-cities_by_state.py)<br>
**Description:** Write a script that lists all cities from the database hbtn_0e_4_usa<br>
**Requirement:** <br>
- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- Results must be displayed as they are in the example below
- Your code should not be executed when imported


### 5. All cities by state

**File:** [5-filter_cities.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/5-filter_cities.py)<br>
**Description:** Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa<br>
**Requirement:** <br>
- Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

### 6. First state model

**File:** [model_state.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/model_state.py)<br>
**Description:** Write a python file that contains the class definition of a State and an instance Base = declarative_base():<br>
**Requirement:** <br>
- State class:
 -- inherits from Base Tips
 -- links to the MySQL table states
 -- class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
 -- class attribute name that represents a column of a string with maximum 128 characters and can’t be null
-- You must use the module SQLAlchemy
-- Your script should connect to a MySQL server running on localhost at port 3306
-- WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)