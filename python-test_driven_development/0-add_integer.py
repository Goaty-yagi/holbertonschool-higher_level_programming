def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
