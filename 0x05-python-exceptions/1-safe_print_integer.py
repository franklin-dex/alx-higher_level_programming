#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

# Example usage:
result = safe_print_integer(42)
print("Print successful:", result)

result = safe_print_integer("Not an integer")
print("Print successful:", result)

