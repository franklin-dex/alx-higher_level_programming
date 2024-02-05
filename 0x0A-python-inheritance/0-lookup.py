#!/usr/bin/python3
""" A func that returns a list of attributes and methods of the given object"""

def lookup(obj):
    """ Returns a list object """
    return dir(obj)
