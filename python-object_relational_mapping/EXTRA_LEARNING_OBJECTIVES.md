# Learning Objectives

- [filter vs filter_by](#filter-vs-filter_by)

## filter vs filter_by 
### **Why filter method doesn't accept id while filter_by does?** 
The reason filter() method doesn't directly accept an id argument while filter_by() does is due to their different purposes and how they are designed to be used.

- filter() method:
The filter() method is designed to accept filtering conditions as expressions. These conditions are usually constructed using SQLAlchemy's operators and functions to specify criteria for selecting rows from the database table.
For example, you might use filter() like this: session.query(Model).filter(Model.id == 2). Here, Model.id == 2 is an expression specifying the filtering condition.

- filter_by() method:

The filter_by() method, on the other hand, is designed to provide a simpler syntax for filtering based on exact column values.
It accepts keyword arguments where the keys correspond to the column names and the values correspond to the filtering conditions.
For example, you might use filter_by() like this: session.query(Model).filter_by(id=2). Here, id=2 specifies that you want to filter rows where the id column has a value of 2.