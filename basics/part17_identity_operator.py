"""
Identity operators in Python :-
Operator        Description                             Example
---------------------------------------------------------------------------------------------------------------------
is              Returns True if both variables          x is y
                represents same object
is not          Returns True if both variables          x is not y
                does not represent same object
---------------------------------------------------------------------------------------------------------------------
Note :- Here same object means both refer to same memory location.
"""
# Example :-
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is y)
print(x is z)
print(x is not y)
print(x == y)
