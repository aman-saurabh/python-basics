"""
1.) Errors :- Errors are the problems in the program or in the system, due to which execution of the program stops.
    Generally errors are irrecoverable and hence can't be handled.But it is not always true
    i.e some errors are recoverable and can be handled like RecursionError.
2.) Exceptions :- Exceptions in Python are special kind of errors that are recoverable and can be handled.
    Generally exceptions are raised when some internal event occur which changes the normal flow of the program
    due to wrong or incorrect logic and hence sometimes exceptions are also known as 'Logical errors'.
    As discussed earlier, exceptions can be handled, but if it is not properly handled, it also force the program to
    terminate abruptly.

Types of errors :-
In python there are mainly 4 types of errors :
1.) SyntaxError
2.) OutOfMemoryError
3.) RecursionError
4.) IndentationError
"""

# Error 1 :- Syntax error(SyntaxError)
# Syntax errors are often caled as parsing errors and are generally caused when the parser
# detects a syntactic issue in the code.For example - if you forget colon(i.e ":") after if statement or a for loop
# or if you forget to put any arithematic or comparison operator between two numerical variables etc.
# Ex :-
a = 8
b = 9
# c = a b
# Above line will throw error since we haven't used any arithmetic or comparison operators in between a and b.

# Error 2 :- Out of memory error(OutOfMemoryError)
# Memory errors are mainly dependent on your system's RAM and are related to Heap.This error mainly occurs if you have
# very large object in the program or loading a large file etc.
# Note :-
# However OutOfMemoryError can be recovered but recovery is not guaranteed. Hence such errors should not be handled.

# Error 3 :- Recursive error
# We will learn it in details in next part.