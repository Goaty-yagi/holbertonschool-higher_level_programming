import doctest


def test_square_area(side_length):
    """
    Test the calculation of the area of a square.

    Input:
        - side_length (float): The length of the side of the square.

    Expected Output:
        - area (float): The calculated area of the square.

    Example Usage:
        >>> test_square_area(3)
        9
        >>> test_square_area(0)
        0

    Edge Cases:
        - Testing with a negative side_length should raise a ValueError.
        >>> test_square_area(-1)
        Traceback (most recent call last):
        ...
        ValueError: side_length must be non-negative
    """
    if side_length < 0:
        raise ValueError("side_length must be non-negative")

    area = side_length ** 2

    # Return the calculated area for validation
    return area
