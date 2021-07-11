"""
Exception2 :- ValueError
Raised when an operator or function receives an argument that has the right type but an inappropriate value.
For example :- int() function accepts a string value and returns corresponding numerical value.
But this is applicable only for such strings which represents a number(i.e number converted into strings).
If we pass such string which does not represent a number to it as argument then it will throw ValueError.
"""
# Ex :-
a = 10
b = int(input("Enter your desired number"))
print(a+b)

# O/P :-
# if we enter -> 20
# output -> 30
# if we enter -> Aman
# output -> ValueError
