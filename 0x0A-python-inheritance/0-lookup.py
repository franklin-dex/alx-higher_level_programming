#!/usr/bin/python3

def lookup(obj):
    """
    Return a list of attributes and methods of a given object
    Args:
        obj: Any python object.
    Returns:
        List[str]: A list containing the names of attributes and methods.
        """
    return dir(obj)
