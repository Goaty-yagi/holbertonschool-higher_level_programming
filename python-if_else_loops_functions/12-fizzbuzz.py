#!/usr/bin/python3

def fizzbuzz():
    fizz = "Fizz"
    buzz = "Buzz"
    for i in range(100):
        i = i + 1
        if i % 3 == 0 and i >= 3:
            print("{}".format(fizz), end=" " if i !=
                  100 and i % 5 != 0 else "")
            if i % 5 != 0:
                continue
        if i % 5 == 0 and i >= 5:
            print("{}".format(buzz), end=" ")
        else:
            print("{}".format(i), end=" ")
