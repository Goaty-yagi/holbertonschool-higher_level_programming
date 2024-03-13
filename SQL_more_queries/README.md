# SQL - More queries
This repository contains advanced SQL queries and examples to help users deepen their understanding of SQL. The queries cover various scenarios, including complex joins, subqueries, and aggregate functions.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc


## Practice Exercises

### 0. My privileges!

**File:** [0-privileges.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/0-privileges.sql)<br>
**Description:** Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost). <br>

### 1. Root user

**File:** [1-create_user.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/1-create_user.sql)<br>
**Description:** Write a script that creates the MySQL server user user_0d_1.<br>
**Requirements:** <br>
- user_0d_1 should have all privileges on your MySQL server
- The user_0d_1 password should be set to user_0d_1_pwd
- If the user user_0d_1 already exists, your script should not fail

### 2. Read user

**File:** [2-create_read_user.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/2-create_read_user.sql)<br>
**Description:** Write a script that creates the database hbtn_0d_2 and the user user_0d_2.<br>
**Requirements:** <br>
- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
- The user_0d_2 password should be set to user_0d_2_pwd
- If the database hbtn_0d_2 already exists, your script should not fail
- If the user user_0d_2 already exists, your script should not fail

### 3. Always a name

**File:** [3-force_name.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/3-force_name.sql)<br>
**Description:** Write a script that creates the table force_name on your MySQL server.<br>
**Requirements:** <br>
- force_name description:
 -- id INT
 -- name VARCHAR(256) can’t be null
- The database name will be passed as an argument of the mysql command
- If the table force_name already exists, your script should not fail

### 4. ID can't be null

**File:** [4-never_empty.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/4-never_empty.sql)<br>
**Description:** Write a script that creates the table id_not_null on your MySQL server.<br>
**Requirements:** <br>
- id_not_null description:
 -- id INT with the default value 1
 -- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table id_not_null already exists, your script should not fail

### 5. Unique ID

**File:** [5-unique_id.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/5-unique_id.sql)<br>
**Description:** Write a script that creates the table unique_id on your MySQL server.<br>
**Requirements:** <br>
- unique_id description:
 -- id INT with the default value 1 and must be unique
 -- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table unique_id already exists, your script should not fail

### 6. States table

**File:** [6-states.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/6-states.sql)<br>
**Description:** Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.<br>
**Requirements:** <br>
- states description:
 -- id INT unique, auto generated, can’t be null and is a -- -- primary key
name VARCHAR(256) can’t be null
- If the database hbtn_0d_usa already exists, your script should not fail
- If the table states already exists, your script should not fail

### 7. Cities table

**File:** [7-cities.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_more_queries/7-cities.sql)<br>
**Description:** Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.<br>
**Requirements:** <br>
- cities description:
 -- id INT unique, auto generated, can’t be null and is a primary key
 -- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
 -- name VARCHAR(256) can’t be null
- If the database hbtn_0d_usa already exists, your script should not fail
- If the table cities already exists, your script should not fail



