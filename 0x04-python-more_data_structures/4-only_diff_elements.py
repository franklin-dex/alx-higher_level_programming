#!/usr/bin/pyhton3
def only_diff_elements(set_1, set_2):
    diff_elements = []

    for element in set_1:
        if element not in set_2 and element not in diff_elements:
            diff_elements.append(element)

    for element in set_2:
        if element not in set_1 and element not in diff_elements:
            diff_elements.append(element)

    return diff_elements
