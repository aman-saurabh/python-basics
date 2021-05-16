"""
Function :-
A function is a block of code that can be run any number of time without defining it repeatedly just by calling it.
Data can also be passed to a function as arguments for further processing
and a function can also return a data as a result.
Syntax of a function :-
-------------------------------------------------------
def function_name(parameter1, parameter2, ...):
    # function_logic
    return resulting_value;
-------------------------------------------------------
So from here it is clear that a function can have any number of parameters(including 0) separated by comma.
And a function can optionally return at most 1 value(i.e if it want it can omit returning value also).
# Difference between argument and parameter :-
The term parameter and argument, both are used for same thing - The information that are passed into a function.
Actually parameters are variables that are listed inside the parenthesis in the function definition
and arguments are data which are passed into the function inside the parenthesis while calling it
i.e Parameters are placeholders for arguments in the method signature.
"""
# Example :-
# Defining the function
def my_function(name):
    return f"Hello {name}!"
# Calling the function
print(my_function("Aman"))

# Standard format of a function :-
# As a good practice every function must be started with a multiline comment describing the details about the function.
# Example :-
def get_sum(num1, num2):
    """
    Author: Aman Saurabh
    Created at: 25 dec, 2020
    :param num1: First number to be added
    :param num2: Second number to be added
    :return: Sum of both numbers
    """
    num = num1+num2
    return num

x = get_sum(5, 12)
print(x)

# Keyword argument in function :-
# You can pass arguments of a function in the form of key-value pair also.
# The main advantage of using this approach is in such scenario, order of the argument does not remain important.
# i.e in case of keyword argument we can pass arguments in any order
# We can pass previous get_sum() function as follows also

y = get_sum(num2=9, num1=17)
print(y)
