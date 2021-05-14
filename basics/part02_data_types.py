# Naming convention for variables as well as methods are snake casing i.e all lower case separated by '_'.
# Avoid using reserved keywords in Python like list, str, int etc.
# Also don't use letters which can create confusion like 'o', 'l', 'I' etc. which can be mistaken to 0 and 1.
# However numbers are allowed for variable names as well as method names but they should not start with a number.

# Data types in python :-
# 1. Integer -> python type -> 'int'
my_int = 5
print(my_int)
# How to check type of a variable in python - There are 2 methods available for this in python.
print(type(my_int))  # Returns the class name of the variable type like "<class 'int'>"
print(isinstance(my_int, int))  # Returns true if the given value(argument 1) is of given type(argument 2)

# Note :- Earlier versions of python used to support 'long' type variable also as '2156L'.
# But now in current versions it doesn't support 'long' type variable(i.e integers with trailing L).
# Now it supports only 'int' type for all integer values, irrespective of their length.
my_long_int = 472188529852923566664231321232123
print(type(my_long_int))

# 2. Complex number -> python type -> 'complex'
# Python also support 'complex' numbers(i.e numbers having real value as well as imaginary value).
# Type of such number is 'complex'.Syntax for such numbers are as follows :
complex_num = 3j + 10
print(type(complex_num))

# 3. Decimal number -> python type -> 'float'
my_float = 10.5
print(type(my_float))

# 4. String -> python type -> 'str'
# In python, just like JS we can define a string using single quote as well as double quote
my_string1 = 'Single colon String'
my_string2 = "Double colon string"
print(type(my_string1))
print(type(my_string2))
print(isinstance(my_string1, str))

# 5. Boolean -> python type -> 'bool'
my_bool = True
print(type(my_bool))
print(isinstance(my_bool, bool))

# 6. List -> python type -> 'list'
# Ordered mutable sequence of objects -> Similar to arrays of other languages
my_list = [10, "Aman", 126.23, False]
print(type(my_list))
print(isinstance(my_list, list))
# Note :-
# Ordered means every item has some fixed position (i.e index) like 1st item has index 0, second item has index 1 etc.
# Unordered means item doesn't have a fixed position.They can be stored in any random position.
# Hence concept of index for items is not supported in Unordered sequences.
# Mutable means items can be modified later at any time after creation and immutable means they can't be modified later.

# 7. Dictionary -> python type -> 'dict'
# Unordered mutable collection of key-value pairs.Keys must be unique i.e can't be duplicated
my_dict = {"key1": "val1", "key2": "val2"}
print(type(my_dict))
print(isinstance(my_dict, dict))

# 8. Set -> python type -> 'set'
# Unordered mutable sequence of unique items.
# Unique means duplicate items are not allowed.
my_set = {"Aman", 654, 0.5, True, 'Geeta'}
print(type(my_set))
print(isinstance(my_set, set))

# 9. Tuple -> python type -> 'tuple'
# Ordered immutable sequence of objects.
my_tuple = (213, "Aman", True, 56.89)
print(type(my_tuple))
print(isinstance(my_tuple, tuple))

# range() function in python :-
"""
range() function is not a datatype in python.
Actually it is a generator function that is used to generate a series of numbers(i.e iterable) within a given range. 
Depending on how many arguments user is passing to the function, 
user can decide where that series of numbers will begin and end as well as 
how big the difference will be between one number and the next.
range() function takes mainly three arguments i.e complete syntax of range() function is as follows :
range(start_point, end_point, incremental_factor)
Here start_point, end_point and incremental_factor all are integral numbers 
and among them only "end_point" is mandatory and other two are optional.
so all valid syntax for range function is as follows:
1.) range(end_point)
2.) range(start_point, end_point)
3.) range(start_point, end_point, incremental_factor)
"""
# Examples :-
# range(end_point)
x = range(10)
print(x)
# range(start_point, end_point)
y = range(2, 10)
print(y)
# range(start_point, end_point, incremental_factor)
z = range(2, 10, 3)
print(z)
# Note :- This range function is mainly used with loops.
# So we will see more appropriate examples of range() function while learing loops through lists, sets etc.
