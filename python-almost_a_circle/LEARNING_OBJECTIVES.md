# Learning Objectives

- [What is Unit testing and how to implement it in a large project](#what-is-unit-utesting-uand-how-to-implement-it-in-a-large-project)
- [How to serialize and deserialize a Class](#how-to-serialize-and-deserialize-a-class)
- [How to write and read a JSON file](#how-to-write-and-read-a-JSON-file)
- [What is *args and how to use it](#what-is-*args-and-how-to-use-it)
- [What is **kwargs and how to use it](#what-is-**kwargs-and-how-to-use-it)
- [How to handle named arguments in a function](#how-to-handle-named-arguments-in-a-function)


## What is Unit testing and how to implement it in a large project

Unit testing is a software testing technique where individual units or components of a software application are tested independently to ensure that works as expected

## How to serialize and deserialize a Class
- 1, set __repr__ method to return the class(not necassary in this case)
- 2, serialize the obj as dict with json.dumps method
- 3, save the dict to a file if necessary.
- 4, open the file and deserialize it with load method
- 5, create a instance with the deserialized dict as args

```python
import json

class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"MyClass(name={self.name}, value={self.value})"

# Create an instance of the class
obj = MyClass(name="example", value=42)

# Serialize the object to JSON
serialized_obj = json.dumps(obj.__dict__)

# Save the serialized object to a file
with open("serialized_object.json", "w") as file:
    json.dump(serialized_obj, file)

# Read the serialized object from the file
with open("serialized_object.json", "r") as file:
    loaded_data = json.load(file)

# Create a new instance of the class using the loaded data
loaded_obj = MyClass(**loaded_data)

# Now, 'loaded_obj' is an instance of the MyClass class
print(loaded_obj)

```
## How to write and read a JSON file
See above
## What is *args and how to use it
*args is a syntax that allows a function to accept a variable number of positional arguments. The *args notation allows a function to receive any number of positional arguments, and those arguments are captured into a tuple.
```python
def func(*args):
    print(type(args))

func(1, 2, 3, 4) # <class 'tuple'>
func([1, 2, 3, 4]) # <class 'tuple'>
func("abcde") # <class 'tuple'>
```
## What is **kwargs and how to use it
**kwargs is a syntax that allows a function to accept a variable number of keyword arguments. The **kwargs notation allows a function to receive any number of keyword arguments, and those arguments are captured into a dictionary.
```python
def print_keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with different numbers of keyword arguments
print_keyword_arguments(first_arg="Value 1", second_arg="Value 2", third_arg="Value 3") # first_arg: Value 1 second_arg: Value 2 third_arg: Value 3
print_keyword_arguments(**{'id':1, 'name':"test"}) # id: 1 name: test
print_keyword_arguments({'id':1, 'name':"test"}) # Will be error TypeError: print_keyword_arguments() takes 0 positional arguments but 1 was given
```
## How to handle named arguments in a function
You can define a function with parameters, and when calling the function, you provide values for these parameters using the syntax parameter_name=value.

```python
def print_info(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

# Call the function with named arguments
print_info(name="John", age=25, country="USA")

```

Also, you can set default args
```python
def print_info_with_defaults(name, age=25, country="Unknown"):
    print(f"Name: {name}, Age: {age}, Country: {country}")

# age and country are optional
print_info_with_defaults("Bob") 
print_info_with_defaults("Alice", country="Canada")
print_info_with_defaults("Eve", age=30, country="Germany")

```