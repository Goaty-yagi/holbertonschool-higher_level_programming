# SQL - Introduction
This repository serves as a beginner-friendly introduction to SQL.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/LEARNING_OBJECTIVES.md) file for details.<br>

[EXTRA_LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/EXTRA_LEARNING_OBJECTIVES.md) file for details.

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

### 0. List databases

**File:** [0-list_databases.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/0-list_databases.sql)<br>
**Description:** Write a script that lists all databases of your MySQL server. <br>


### 1. Create a database

**File:** [1-create_database_if_missing.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/1-create_database_if_missing.sql)<br>
**Description:** Write a script that creates the database hbtn_0c_0 in your MySQL server. <br>
**Requirements:** <br>
- If the database hbtn_0c_0 already exists, your script should not fail
- You are not allowed to use the SELECT or SHOW statements

### 2. Delete a database

**File:** [2-remove_database.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/2-remove_database.sql)<br>
**Description:** Write a script that deletes the database hbtn_0c_0 in your MySQL server. <br>
**Requirements:** <br>
- If the database hbtn_0c_0 doesn’t exist, your script should not fail
- You are not allowed to use the SELECT or SHOW statements

### 3. List tables

**File:** [3-list_tables.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/3-list_tables.sql)<br>
**Description:** Write a script that lists all the tables of a database in your MySQL server. <br>
**Requirements:** <br>
- The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

### 4. First table

**File:** [4-first_table.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/4-first_table.sql)<br>
**Description:** Write a script that creates a table called first_table in the current database in your MySQL server. <br>
**Requirements:** <br>
- first_table description:
 -- id INT
 -- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table first_table already exists, your script should not fail
- You are not allowed to use the SELECT or SHOW statements

### 5. Full description

**File:** [5-full_table.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/5-full_table.sql)<br>
**Description:** Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server. <br>
**Requirements:** <br>
- The database name will be passed as an argument of the mysql command
- You are not allowed to use the DESCRIBE or EXPLAIN statements

### 6. List all in table

**File:** [6-list_values.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/6-list_values.sql)<br>
**Description:** Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server. <br>
**Requirements:** <br>
- All fields should be printed
- The database name will be passed as an argument of the mysql command

### 7. First add

**File:** [7-insert_value.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/7-insert_value.sql)<br>
**Description:** Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server. <br>
**Requirements:** <br>
- New row:
-- id = 89
-- name = Best School
- The database name will be passed as an argument of the mysql command

### 8. Count 89


**File:** [8-count_89.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/8-count_89.sql)<br>
**Description:** Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server. <br>
**Requirements:** <br>
- The database name will be passed as an argument of the mysql command

### 9. Full creation


**File:** [9-full_creation.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/9-full_creation.sql)<br>
**Description:** Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows. <br>
**Requirements:** <br>
- second_table description:
 -- id INT
 -- name VARCHAR(256)
 -- score INT
- The database name will be passed as an argument to the mysql command
- If the table second_table already exists, your script should not fail
- You are not allowed to use the SELECT and SHOW statements
- Your script should create these records:
 -- id = 1, name = “John”, score = 10
 -- id = 2, name = “Alex”, score = 3
 -- id = 3, name = “Bob”, score = 14
 -- id = 4, name = “George”, score = 8


### 10. List by best

**File:** [10-top_score.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/10-top_score.sql)<br>
**Description:** Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. <br>
**Requirements:** <br>
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the mysql command

### 11. Select the best

**File:** [11-best_score.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/11-best_score.sql)<br>
**Description:** Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.<br>
**Requirements:** <br>
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the mysql command

### 12. Cheating is bad

**File:** [12-no_cheating.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/12-no_cheating.sql)<br>
**Description:** Write a script that updates the score of Bob to 10 in the table second_table.<br>
**Requirements:** <br>
- You are not allowed to use Bob’s id value, only the name field
- The database name will be passed as an argument of the mysql command

### 13. Score too low

**File:** [13-change_class.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/13-change_class.sql)<br>
**Description:** Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.<br>
**Requirements:** <br>
- The database name will be passed as an argument of the mysql command

### 14. Average

**File:** [14-average.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/14-average.sql)<br>
**Description:** Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.<br>
**Requirements:** <br>
- The result column name should be average
- The database name will be passed as an argument of the mysql command

### 15. Number by score

**File:** [15-groups.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/15-groups.sql)<br>
**Description:** Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.<br>
**Requirements:** <br>
- The result should display:
 -- the score
 -- the number of records for this score with the label number
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the mysql command


### 16. Say my name

**File:** [16-no_link.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/16-no_link.sql)<br>
**Description:** Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.<br>
**Requirements:** <br>
- Don’t list rows without a name value
- Results should display the score and the name (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the mysql command


### 17. Go to UTF8

**File:** [100-move_to_utf8.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/100-move_to_utf8.sql)<br>
**Description:** Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.<br>
**Requirements:** <br>
- You need to convert all of the following to UTF8:
 -- Database hbtn_0c_0
 -- Table first_table
 -- Field name in first_table


### 18. Temperatures #0

**File:** [101-avg_temperatures.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/101-avg_temperatures.sql)<br>
**Description:** Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).<br>
```bash
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
```

### 19. Temperatures #1

**File:** [102-top_city.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/102-top_city.sql)<br>
**Description:** Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).<br>