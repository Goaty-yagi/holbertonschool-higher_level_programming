#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    t_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    t_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    new_tuple = (t_a[0] + t_b[0], t_a[1] + t_b[1])
    return (new_tuple)
