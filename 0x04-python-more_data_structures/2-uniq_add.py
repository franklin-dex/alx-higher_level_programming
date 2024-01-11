#!/usr/bin/python3

def uniq_add(my_list=[]):
    seen = []
    total_sum = 0

    for element in my_list:
        if element not in seen:
            seen.append(element)
            total_sum += element

    return total_sum
