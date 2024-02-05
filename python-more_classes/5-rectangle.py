#!/usr/bin/python3

"""
This module defines a basic Rectangle class.
Classes:
    - Rectangle: A class representing a rectangle.
"""


class Rectangle:
    """
    Rectangle Class

    A basic representation of a rectangle with width and height attributes.

    Attributes:
        - ATTR_NAMES (dict): A dictionary mapping attribute names to
        their string representations.

    Methods:
        - __init__(self, width: int = 0, height: int = 0) -> None:
        Constructor to initialize the rectangle's width and height.
        - __str__(self) -> str:
        String representation of the rectangle, representing it as a
        sequence of "#" characters forming a rectangle.
        - __repr__(self) -> str:
        Formal string representation of the rectangle.
         - __del__(self) -> None:
        Print when an instance is deleted.
        - attributes_setter(self, value: int, name: str) -> int:
        Helper method to set and validate attribute values.
        - width(self) -> int:
        Getter method for the rectangle's width attribute.
        - width(self, value: int) -> None:
        Setter method for the rectangle's width attribute.
        - height(self) -> int:
        Getter method for the rectangle's height attribute.
        - height(self, value: int) -> None:
        Setter method for the rectangle's height attribute.
        - area(self) -> int:
        Method to calculate the area of the rectangle.
        - perimeter(self) -> int:
        Method to calculate the perimeter of the rectangle.
    """

    ATTR_NAMES = {
        "WIDTH": "width",
        "HEIGHT": "height"
    }

    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.__height = self.attributes_setter(
            height, Rectangle.ATTR_NAMES["HEIGHT"])

        self.__width = self.attributes_setter(
            width, Rectangle.ATTR_NAMES["WIDTH"])

    def __str__(self) -> str:
        if any(value == 0 for value in (self.__width, self.__height)):
            return ""
        map_obj = map(lambda x: "#\n" if self.area() != x and x %
                      self.__width == 0 else "#", range(1, self.area() + 1))
        return "".join(map_obj)

    def __repr__(self) -> str:
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")

    def attributes_setter(self, value: int, name: str) -> int:
        if isinstance(value, int):
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
            if name == Rectangle.ATTR_NAMES["WIDTH"]:
                self.__width = value
            else:
                self.__height = value
            return value
        else:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        self.attributes_setter(value, Rectangle.ATTR_NAMES["WIDTH"])

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value) -> None:
        self.attributes_setter(value, Rectangle.ATTR_NAMES["HEIGHT"])

    def area(self) -> int:
        return self.__width * self.__height

    def perimeter(self) -> int:
        if any(value == 0 for value in (self.__width, self.__height)):
            return 0
        return self.__width * 2 + self.__height * 2
