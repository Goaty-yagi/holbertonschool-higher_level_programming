# Learning Objectives

- [What is a superclass, baseclass or parentclass](#what-is-a-superclass,-baseclass-or-parentclass)
- [What is a subclass](#what-is-a-subclass)
- [How to list all attributes and methods of a class or instance](#how-to-list-all-attributes-and-methods-of-a-class-or-instance)
- [When can an instance have new attributes](#when-can-an-instance-have-new-attributes)
- [How to inherit class from another](#how-to-inherit-class-from-another)
- [How to define a class with multiple base classes](#how-to-define-a-class-with-multiple-base-classes)
- [What is the default class every class inherit from](#what-is-the-default-class-every-class-inherit-from)
- [How to override a method or attribute inherited from the base class](#how-to-override-a-method-or-attribute-inherited-from-the-base-class)
- [Which attributes or methods are available by heritage to subclasses](#which-attributes-or-methods-are-available-by-heritage-to-subclasses)
- [What is the purpose of inheritance](#what-is-the-purpose-of-inheritance)
- [What are, when and how to use isinstance, issubclass, type and super built-in functions](#what-are,-when-and-how-to-use-isinstance,-issubclass,-type-and-super-built-in-functions)

## What is a superclass, baseclass or parentclass
In Python, the terms superclass, base class, and parent class are used interchangeably to refer to a class that is being inherited by another class. 
## What is a subclass
Subclass, derived class, and child class are terms used for the class that is inheriting from another class.
## How to list all attributes and methods of a class or instance
dir()
## When can an instance have new attributes
In Python, instances can have new attributes added at any point during their lifetime.

- During Initialization (In the Constructor):
```python
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create an instance and add a new attribute during initialization
my_instance = MyClass(10, 20)
my_instance.z = 30

```

- After Initialization (Anywhere in the Code):
```python
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create an instance
my_instance = MyClass(10, 20)

# Add a new attribute after initialization
my_instance.z = 30

```
- In the setter method
```python
class MyClass:
    def __init__(self, x):
        self._x = x  # Note the use of a private attribute with a leading underscore

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        # Add any validation logic or additional actions here
        if value < 0:
            raise ValueError("x must be a non-negative value")
        self._x = value

# Create an instance
my_instance = MyClass(5)

# Access the attribute using the getter
print(my_instance.x)  # Output: 5

# Use the setter to change the attribute value
my_instance.x = 10

# Access the updated attribute
print(my_instance.x)  # Output: 10

# Trying to set an invalid value will raise an exception
# my_instance.x = -3  # Uncommenting this line would raise a ValueError

```
## How to inherit class from another
You can inherit a class from another class by specifying the parent class(es) in the class definition.
```python
class ParentClass:
    # Parent class code

class ChildClass(ParentClass):
    # Child class code

```
## How to define a class with multiple base classes
You can define a class with multiple base classes by listing them within parentheses in the class definition
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Mammal:
    def give_birth(self):
        print(f"{self.name} gives birth to live young")

# Multiple inheritance
class Dog(Animal, Mammal):
    def bark(self):
        print(f"{self.name} barks")

# Creating an instance of the derived class
my_dog = Dog("Buddy")

# Accessing methods from both base classes and the derived class
my_dog.speak()          # Output: Buddy makes a sound
my_dog.give_birth()     # Output: Buddy gives birth to live young
my_dog.bark()           # Output: Buddy barks

```
## What is the default class every class inherit from
In Python, every class implicitly inherits from a built-in class called object. The object class is the base class for all classes in Python. If a class definition does not explicitly inherit from any other class, it automatically inherits from object.
```python
class MyClass:
    # Class code

# Equivalent to:
# class MyClass(object):
#     # Class code

```
## How to override a method or attribute inherited from the base class
You can override a method or attribute inherited from a base class in a derived class by providing a new implementation for that method or attribute in the derived class. 

- Method orverriding
```python
class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Creating instances
generic_animal = Animal()
my_dog = Dog()

# Calling the speak method on instances
generic_animal.speak()  # Output: Generic animal sound
my_dog.speak()          # Output: Woof!

```

- With super
```python
class Shape:
    def __init__(self, color):
        self.color = color

class Square(Shape):
    def __init__(self, side_length, color):
        super().__init__(color)
        self.side_length = side_length

# Creating instances
red_square = Square(5, "red")

# Accessing attributes
print(red_square.color)        # Output: red (inherited from Shape)
print(red_square.side_length)  # Output: 5 (defined in Square)

```

## Which attributes or methods are available by heritage to subclasses
When a subclass inherits from a parent class, it gains access to all the attributes and methods of that parent class.
## What is the purpose of inheritance
- Code Reusability:
Inheritance promotes code reuse by allowing a subclass to inherit the attributes and methods of a superclass. Instead of rewriting code, developers can build upon existing functionality.

- Modularity:
Inheritance supports modularity in software design. Classes can be divided into smaller, more manageable units (superclasses and subclasses), making it easier to understand, develop, and maintain complex systems.

- Extensibility:
Subclasses can extend or enhance the functionality of the superclass by adding new attributes or methods, or by overriding existing methods. This facilitates the addition of new features without modifying the original code.

- Polymorphism:
Inheritance enables polymorphism, allowing objects of a subclass to be treated as objects of the superclass. This promotes flexibility in designing and using classes, supporting a more generalized and abstract approach to programming.

- Encapsulation:
Inheritance, along with encapsulation, helps in organizing and structuring code. It allows the hiding of implementation details within the class, exposing only the necessary interfaces. Subclasses can access the public and protected members of the superclass.

- Hierarchy and Classification:
Inheritance provides a way to model real-world relationships and hierarchies. For example, a base class "Vehicle" might have subclasses like "Car" and "Motorcycle." This modeling reflects the natural hierarchy of objects.

- Method Overriding:
Subclasses can override (provide a new implementation for) methods inherited from the superclass. This allows customization of behavior in subclasses while maintaining a consistent interface.

- Simplifying Complexity:
Inheritance simplifies the complexity of code by organizing related classes in a hierarchy. It enhances code readability and makes it easier for developers to understand the relationships between classes.

- Maintenance:
Inheritance supports easier maintenance of code. Changes made to the superclass automatically affect all its subclasses. This reduces the chances of errors and ensures consistency in the application.

## What are, when and how to use isinstance, issubclass, type and super built-in functions

The built-in functions isinstance, issubclass, type, and super in Python are commonly used in object-oriented programming. 

- isinstance(object, classinfo):
Determines if an object is an instance of a particular class or a tuple of classes.

- issubclass(class, classinfo):
Checks if a class is a subclass of another class or a tuple of classes.

- type(object):
Returns the type of an object.

- super():
Returns a temporary object of the superclass to allow access to its methods.