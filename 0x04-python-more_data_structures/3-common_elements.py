#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_elements = []

    for element in set_1:
        if element in set_2 and element not in common_elements:
            common_elements.append(element)

    return common_elements
