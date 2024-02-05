# Learning Objectives

- [What are the special __str__ and __repr__ methods and how to use them](#what-are-the-special-__str__-and-__repr__-methods-andhow-to-use-them)
- [What is the difference between __str__ and __repr__](#what-is-the-difference-between-__str__-and-__repr__)
- [What is a class attribute](#what-is-a-class-attribute)
- [What is the difference between a object attribute and a class attribute](#what-is-the-difference-between-a-object-attribute-and-a-class-attribute)
- [What is a class method](#what-is-a-class-method)
- [What is a static method](#what-is-a-static-method)
- [What is and what does contain __dict__ of a class and of an instance of a class](#what-is-and-what-does-contain-__dict__-of-a-class-and-of-an-instance-of-a-class)


## 1, What are the special __str__ and __repr__ methods and how to use them

### __str__ Method:

To define the informal or user-friendly string representation of an object.
This method is called by the str() function and the print() function.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"The value is {self.value}"

obj = MyClass(42)
print(str(obj))  # Output: The value is 42

```

### __repr__ Method:

To define the official or developer-friendly string representation of an object. It should ideally be a valid Python expression that, when executed(eval()), would recreate the object.
This method is called by the repr() function and is often used for debugging and logging.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyClass({self.value})"

obj = MyClass(42)
repr_string = repr(obj)
print(repr(obj))  # Output: MyClass(42)

# You can make a new obj with the same attributes
new_obj = eval(repr_string)


```

## 2, What is the difference between __str__ and __repr__

- __str__ is focused on providing a readable and user-friendly representation for end-users. It's used by str() and print() functions.
- __repr__ is focused on providing a detailed and unambiguous representation for developers. It's used by repr() function and in debugging contexts.

If __str__ is not defined for a class, Python falls back to __repr__ when trying to obtain a string representation for end-users.
It's common to define both methods in a class, with __repr__ providing a more detailed representation and __str__ offering a more readable representation.


## 3, What is a class attribute

A class attribute in Python is a variable that is associated with a class rather than an instance of the class (object). Class attributes are shared among all instances (objects) of the class and are defined outside of any class methods. They are accessed using the class name rather than an instance.

```python
class MyClass:
    class_attribute = 42  # This is a class attribute

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

# Accessing the class attribute using the class name
print(MyClass.class_attribute)  # Output: 42

# Creating instances of the class
obj1 = MyClass(10)
obj2 = MyClass(20)

# Accessing the class attribute using instances
print(obj1.class_attribute)  # Output: 42
print(obj2.class_attribute)  # Output: 42

# Modifying the class attribute using the class name
MyClass.class_attribute = 99

# Accessing the modified class attribute through an instance
print(obj1.class_attribute)  # Output: 99
print(obj2.class_attribute)  # Output: 99

```

## What is the difference between a object attribute and a class attribute

### Object Attribute:

- Scope: Object attributes are specific to each instance of a class. Each instance can have its own set of object attributes.
- Definition: Object attributes are defined within the methods of a class, typically within the __init__ method, and they are accessed using the self keyword.
- Access: Object attributes are accessed using the instance of the class, and changes made to an object attribute only affect that particular instance.

### Class Attribute:

- Scope: Class attributes are shared among all instances of a class. They are associated with the class itself rather than with individual instances.
- Definition: Class attributes are defined outside of any class method, typically at the class level, and they are accessed using the class name.
- Access: Class attributes are accessed using either the class name or an instance of the class. Changes made to a class attribute are reflected in all instances of the 

## What is a class method

A class method  is a method that is bound to the class and not the instance of the class. It is defined using the @classmethod decorator and takes the class itself (cls) as its first parameter instead of the instance (self). Class methods are typically used for operations that are related to the class rather than instances, such as creating class-level attributes, accessing or modifying class-level data, or performing operations that don't require access to instance-specific data.

```python
class MyClass:
    class_attribute = 42  # Class attribute

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    @classmethod
    def create_instance(cls, value):
        # Creating an instance of the class using the class method
        return cls(value)

# Using the class method to create an instance
obj = MyClass.create_instance(10)

# Accessing instance and class attributes
print(obj.instance_attribute)      # Output: 10
print(obj.class_attribute)         # Output: 42

# Creating another instance using the class method
obj2 = MyClass.create_instance(20)
print(obj2.instance_attribute)     # Output: 20
print(obj2.class_attribute)        # Output: 42

```

## What is a static method

A static method is a method that belongs to a class rather than an instance of the class. Unlike regular methods and class methods, static methods don't have access to the instance or the class itself as their first parameter (self or cls). They are defined using the @staticmethod decorator and are typically used for operations that don't depend on instance-specific or class-specific data.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Using static methods through the class
result_add_class = MathOperations.add(3, 5)
result_multiply_class = MathOperations.multiply(4, 6)

print(result_add_class)       # Output: 8
print(result_multiply_class)  # Output: 24

# Creating an instance
obj = MathOperations()

# Using static methods through the instance
result_add_instance = obj.add(7, 2)
result_multiply_instance = obj.multiply(3, 4)

print(result_add_instance)       # Output: 9
print(result_multiply_instance)  # Output: 12

```

## What is and what does contain __dict__ of a class and of an instance of a class

The __dict__ attribute is a dictionary that contains the namespace of a class or an instance. It holds the attributes (including methods) of the class or instance, allowing you to access, modify, or add attributes dynamically.