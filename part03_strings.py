# Strings are ordered immutable sequence of characters i.e each character of a string has unique index
# and once string is created, we can't alter its content, however we can create a new string
# with few characters of existing one or by replacing few characters of existing one.

# String slicing :-
"""
Format -> string[x:y:z] => x -> start_index(including), y -> end_index(excluding), z -> interval
Interval in z means (z-1) gap between two elements.
i.e z=1 means all elements,z=2 means pick one element and skip one, z=3 means pick one element and skip two and so on.
and negative z means move in opposite direction i.e from end to start(interval rule will be same as positive z).
"""

my_str = "abcdefghijklmnop"
print(my_str[3])
# d
print(my_str[3:])
# defghijklmnop
print(my_str[3:7])
# defg
print(my_str[:7])
# abcdefg
print(my_str[::])
# abcdefghijklmnop
print(my_str[2:13:1])
# cdefghijklm
print(my_str[2:13:3])
# cfil
print(my_str[::3])
# adgjmp
print(my_str[:2:])
# ab
print(my_str[-10:-3])
# ghijklm
print(my_str[13:3:-2])
# nljhf
print(my_str[-13:-3:-2])
# Will no produce any result as in case of negative z, x should be greater than y
print(my_str[-3:-13:-2])
# nljhf

# String interpolation :-
"""
String interpolation is a process of substituting values of a variable into placeholders in a string.
There are several methods available for this purpose in Python.
Here we mill discuss two main methods which are very widely used.
1.) string.format()
2.) f-strings 
Note that among them 'f-strings' was introduced in Python 3.6 version and hence it is more advance.
We can perform several operations on variables directly in 'f-strings' which is not possible in string.format(). 
"""
# variables to be used in string.format() as well as f-strings :-
name = "Aman"
city = "Noida"
# string.format() :-
print('Hi, My name is {}, and I am from {}.'.format(name, city))

# f-strings :-
print(f'Hi, My name is {name}, and I am from {city}')

# Another example of f-string which is not directly possible with string.format() :
a = 5
b = 7
print(f'Multiplication of given numbers : {a*b}.')

