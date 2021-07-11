"""
Error 4:- indentation error(IndentationError)
Indentation error is similar to SyntaxError in spirit and falls under it.
However it is specific to only indentation related issues in the script.
Indentation errors are irrecoverable and hence should not be handled.
"""
# Example :-
def my_func():
    try:
        print("My function called")     # Change it's indentation to get the error and test IndentationError.
    except IndentationError:
        print("Indentation error occured")

my_func()

"""
So from here we can see that there is no use of handling IndentationError.
"""