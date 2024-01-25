#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    text = "argument" if len(arguments) == 1 else "arguments"
    has_attr = "." if len(arguments) == 0 else ":"
    print("{} {}{}".format(len(arguments), text, has_attr))

    for i in range(len(arguments)):
        print("{}: {}".format(i + 1, arguments[i]))
