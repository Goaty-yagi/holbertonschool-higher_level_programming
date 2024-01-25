#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    result = 0

    for i in range(len(arguments)):
        result = result + int(arguments[i])

    print("{}".format(result))
