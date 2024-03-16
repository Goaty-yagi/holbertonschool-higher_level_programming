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
- 1, create new object
- 2, open session
- 3, add the obj to session by add method
- 4, session commit by commit method

Example

```python
# Create new State object
    new_state = State(name='Louisiana')


    with Session() as session:
        # Add the new State object to the session
        session.add(new_state)
        session.commit()
```

## What ORM means
ORM stands for Object-Relational Mapping. It's a programming technique used to convert data between incompatible type systems – in particular, between relational databases and object-oriented programming languages like Python, Java, or C#.
## How to map a Python Class to a MySQL table
- 1, import sqlalchemy
- 2, make Base class from declarative_base
- 3, create class inherited from the Base class
- 4, set columns with certain arguments
- 5, create engine with username, passwords and db name
- 6, create DB with the engine by Base.metadata.create_all method

Example
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

```

