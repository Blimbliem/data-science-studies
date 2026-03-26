# when something gets wrong, we can raise an exception, and in python we use the 'try' and 'except' expression to handle exceptions

try:
    print(10/0) # this will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero!") 