
#each function receive zero or more arguments and return a value, by default, in python when we created a function, we use 'def'

def double (x):
    """"
    hear, we explain what the function does, but this step is optional, but it is a good practice to include a docstring that describes the purpose of the function, its parameters, and its return value. This helps other developers understand how to use the function and what to expect from it.
    This function takes a number as input and returns its double.
    Parameters:
    x (int or float): The number to be doubled.
    Returns:
    int or float: The double of the input number.
    """
    return x * 2

#first class function

def apply_function(f):
    """"
    we can put in variables the functions, and we can pass them as arguments to other functions"""
    return f(1)

my_double = double

x = apply_function(my_double)
print(x)

# anonymous function, also know as lambda function:

y = apply_function(lambda x: x + 3)
print(y)


#parameters and arguments:

def my_print(message ="my default message"):
    print(message)

my_print("hello world")
my_print()