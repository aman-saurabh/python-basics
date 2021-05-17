"""
Identity operators in Python :-
Operator        Description                             Example
---------------------------------------------------------------------------------------------------------------------
in              Returns True if a sequence with         x in y
                the specified value is present
                in the given object
not in          Returns True if a sequence with         x not in y
                the specified value is not present
                in the given object
---------------------------------------------------------------------------------------------------------------------
"""
# Example1 :-
x = ["apple", "banana"]
print("banana" in x)
print("apple" not in x)
print("grape" not in x)

# Example2 :-
y = "Github"
print("Git" in y)
print("git" not in y)
