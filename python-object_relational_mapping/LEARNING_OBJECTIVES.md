# Learning Objectives

-  [How to connect to a MySQL database from a Python script](#How-to-connect-to-a-MySQL-database-from-a-Python-script)
-  [How to SELECT rows in a MySQL table from a Python script](#How-to-SELECT-rows-in-a-MySQL-table-from-a-Python-script)
-  [How to INSERT rows in a MySQL table from a Python script](#How-to-INSERT-rows-in-a-MySQL-table-from-a-Python-script)
-  [What ORM means](#What-ORM-means)
-  [How to map a Python Class to a MySQL table](#How-to-map-a-Python-Class-to-a-MySQL-table)

## How to connect to a MySQL database from a Python script
### 1, Install MySql 
```bash
apt update
apt install mysql-server
```
### 2, Install related packages
```bash
apt-get install python3-dev
apt-get install libmysqlclient-dev
apt-get install zlib1g-dev

```
### 3, Install mysqlclient

```bash
pip3 install mysqlclient
```
### 4, import MySQLdb, and set configurations

```python
import MySQLdb
connection = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
```
## How to SELECT rows in a MySQL table from a Python script
Make a cursor from the connection above, and set SQL script
```python
with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM states ORDER BY states.id")
```
## How to INSERT rows in a MySQL table from a Python script
## What ORM means
ORM stands for Object-Relational Mapping. It's a programming technique used to convert data between incompatible type systems – in particular, between relational databases and object-oriented programming languages like Python, Java, or C#.
## How to map a Python Class to a MySQL table

