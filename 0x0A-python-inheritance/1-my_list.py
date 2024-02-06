#!/usr/bin/python3
"""A class MyList that inherits from list."""

class Mylist(list):
    """custom listt class with additional methods"""

    def print_sorted(self):
        """print the list sorted in accending order"""

        print(sorted(self))
