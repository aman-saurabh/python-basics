"""
Python provides many built-in functions that are predefined and can be used by the end-user by just calling them.
These functions not just ease the work of programmers but also create a standard coding environment.
map(), filter and reduce() are also 3 such inbuilt functions of Python.
These functions enable the functional programming aspect of Python.
In functional programming's pure functions, the arguments passed are the only factors that decide upon the output.
All these functions can take any other function as a parameter and can be supplied to other functions as parameters.
Infact all these 3 functions requires a function as the first parameter
(We will learn about their complete syntax and other details later, for now let's focus on lambda functions).
Most of the time, the function, which we supply to these functions(i.e map(), filter() and reduce() functions)
will not be required anywhere else i.e they are single use functions used exclusively with these functions.
So for such requirement creating a separate user-defined function makes no sense.

It would be better if we can write logic of such single use function directly within these functions itself.
And there comes lambda functions into the picture.
Actually lambda functions are functions with single expression and without a name.
Hence they are also known as 'single expression functions' and 'anonymous functions'.
Infact the word ‘lambda’ is not a name, but its a keyword.
This keyword specifies that the function that follows is an anonymous function.
As we have already discussed that a lambda function can contain only one expression and with that expression only
it has to return the processed value, so in lambda functions there is no need of using 'return' keyword explicitly.

Syntax of lambda function :-
lambda arguments: expression
"""

# Ex1 :-
# Normal function
def get_sum(a, b):
    return a + b
print(get_sum(5, 7))

# Equivalent lambda function
lambda a, b: a + b

# We can hold this lambda function in a variable and call it whenever we want like normal functions.Ex :
my_sum = lambda a, b: a + b
print(my_sum(5, 7))


# But this is not recommended. If you need to hold it in a variable to call later then use normal function instead.
# And if you are creating this lambda function to pass it as argument in map(), filter() and reduce() functions,
# then you will not need to hold it any variable.You can directly define it inside these function parenthesis itself.

# Ex2 :-
# Normal function
def starts_with(str):
    return "Vowel" if str.lower()[0] in ['a', 'e', 'i', 'o', 'u'] else "Consonant"
print(starts_with("Aman"))
print(starts_with("Manish"))

# Equivalent lambda function (holding it in a variable to call it later)
check_starts_with = lambda str: "Vowel" if str.lower()[0] in ['a', 'e', 'i', 'o', 'u'] else "Consonant"
print(check_starts_with("Aman"))
print(check_starts_with("Manish"))

# Ex3 :- (Lambda expression inside normal function)
# Write a program to get square and cube of given number.
# We have divided the problem in 2 parts and solved both parts with 2 methods.

# Part1 :-
# Method1 :-
"""
get_square = lambda n: n ** 2
get_cube = lambda n: n ** 3
"""
# Method2 :-
# Same functionality we can achieve as follows :-
def get_power(n):
    return lambda a: a ** n
# Here it is not returning a normal expression but a function itself. Particularly a lambda function.
get_square = get_power(2)
get_cube = get_power(3)

# Part2 :-
# Method 1 :-
"""
def get_square_cube(num):
    square = get_square(num)
    cube = get_cube(num)
    return square, cube
"""
# Method 2 :-
get_square_cube = lambda num: (get_square(num), get_cube(num))
print(get_square_cube(6))
