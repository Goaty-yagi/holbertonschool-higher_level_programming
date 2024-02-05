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
        - number_of_instances (int) : an integer representing
        number of existing instants
        - print_symbol (any) : a symbol to be used
        for string representation

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

    number_of_instances: int = 0
    print_symbol: any = "#"

    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.__height = self.attributes_setter(
            height, Rectangle.ATTR_NAMES["HEIGHT"])

        self.__width = self.attributes_setter(
            width, Rectangle.ATTR_NAMES["WIDTH"])

        Rectangle.number_of_instances += 1

    def __str__(self) -> str:
        if any(value == 0 for value in (self.__width, self.__height)):
            return ""
        map_obj = map(lambda x: "{}\n".format(self.print_symbol)
                      if self.area() != x and x % self.__width == 0 else "{}"
                      .format(self.print_symbol), range(1, self.area() + 1))
        return "".join(map_obj)

    def __repr__(self) -> str:
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self) -> None:
        Rectangle.number_of_instances -= 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        error_arg = ""
        error_message = " must be an instance of Rectangle"

        if not isinstance(rect_1, Rectangle):
            error_arg = "rect_1"
        elif not isinstance(rect_2, Rectangle):
            error_arg = "rect_2"
        if error_arg:
            raise TypeError(error_arg + error_message)

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

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
