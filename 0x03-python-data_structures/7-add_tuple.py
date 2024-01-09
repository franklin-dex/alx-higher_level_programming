#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    sum_a, sum_b = 0, 0

    for i in range(min(len(tuple_a), len(tuple_b))):
        sum_a += tuple_a[i] if i < len(tuple_a) else 0
        sum_b += tuple_b[i] if i < len(tuple_b) else 0

    return (sum_a, sum_b)
