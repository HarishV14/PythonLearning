def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
 
    # return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)



def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """
    return a * b
print(multiply_numbers(3,5))