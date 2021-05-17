# Normal if-else statements :-
a = 120
b = 30

if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("a is less than b")

# short hand "if" statement :-
if a > b:
    print("a is greater than b")

# short hand "if-else" statement :-
print("a is greater than b") if a > b else print("a is less than or equal to b")

# short hand "if-elif-else" statement :-4
print("a is greater than b") if a > b else print("a and b are equal") if a == b else print("a is less than b")
