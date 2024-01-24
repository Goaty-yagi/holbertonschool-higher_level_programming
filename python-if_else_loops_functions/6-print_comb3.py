#!/usr/bin/python3

for i in range(10):
    for n in range(10):
        if i < n:
            print("{}{}".format(i, n), end=", " if i != 8 else "\n")
