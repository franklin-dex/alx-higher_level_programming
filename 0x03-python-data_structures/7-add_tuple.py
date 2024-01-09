#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    min_length = min(len(tuple_a), len(tuple_b))
    tuple_a += (0,) * (2 - len(tuple_a))
    tuple_b += (0,) * (2 - len(tuple_b))

    return tuple(a + b for a, b in zip(tuple_a[:2], tuple_b[:2]))
