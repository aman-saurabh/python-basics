"""
Logical operators in Python :-
Operator        Description                             Example
---------------------------------------------------------------------------------------------------------------------
and             Returns true if both                    x > 5 and x < 10
                statements are true                     (if x = 7 returns True and if x = 3 returns False)
---------------------------------------------------------------------------------------------------------------------
or              Returns true if any of                  1.) x <5 or x > 10
                the statement is true                   (if x = 7 returns False and if x = 3 or x = 13 returns True)
---------------------------------------------------------------------------------------------------------------------
not             Returns true if result of the           not(x > 5 and x < 10)
                internal expression is false            (if x = 7 returns False and if x = 3 returns True)
                                                        not y==7
                                                        (if y =3 returns True and if y = 7 returns False)
---------------------------------------------------------------------------------------------------------------------
"""

# Example :-
x = 15
y = 20
z = x

print(y > x and z < y)
print(y > x or z < y)
print(not(y > x and z < y))
print(not x == z)



