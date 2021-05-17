"""
In python, a function can call any other function, So it can call itself as well.
The process of, a function calling itself is known as "function recursion".
And functions which call itself in the method definition is known as "Recursive function".
"""
# Example :-
def my_function(num):
    if num > 0:
        print("Count is :", num)
        my_function(num-1)
    else:
        print("Now count is 0")

my_function(6)
