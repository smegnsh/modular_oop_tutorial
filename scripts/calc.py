'''# calc.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

'''
#refactor
# Internal helper function to validate that inputs are numbers
def _validate_numbers(a, b):
    # Check if both inputs are either int or float types
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Raise error if inputs are invalid types
        raise TypeError("Inputs must be numbers")


# Add function using validation
def add(a, b):
    # Validate inputs before performing addition
    _validate_numbers(a, b)
    # Return the sum
    return a + b


# Subtract function using validation
def subtract(a, b):
    # Validate both inputs
    _validate_numbers(a, b)
    # Return the difference
    return a - b


# Multiply function using validation
def multiply(a, b):
    # Validate inputs
    _validate_numbers(a, b)
    # Return the product
    return a * b


# Divide function using validation
def divide(a, b):
    # Validate both numbers
    _validate_numbers(a, b)
    # Check for division by zero
    if b == 0:
        # Raise ZeroDivisionError if denominator is zero
        raise ZeroDivisionError("Cannot divide by zero")
    # Perform division and return result
    return a / b
