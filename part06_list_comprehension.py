import math

"""
list comprehension offers a shorter syntax to create a list based on values of existing list or range function.
Complete syntax of list comprehension :-
new_list = ['expression' for 'member' in 'iterable' (optional 'conditions')]
where
1.) expression :- expression can be any valid expression based on member for example suppose if member is 'i' then
expression can be 'i*i', 'i+5-3' etc. or 'i' itself (in case we want same values in the list as in specified iterable).
2.) member :- Member represents each item present in the iterable(one by one).
3.) iterable :- iterable can be anything which contains or can generate a sequence of items.
like list, set, tuple, sequence generator like range() method, strings etc.
4.) condition :- condition can be any valid 'if' condition.They are optional and used to filter out unwanted values.

Before we see examples of list comprehension first learn about range() function.
Actually range() function is a pre-defined function provided my Python used to generate a sequence of numbers.
Complete syntax of range() function :- range(start_value, end_value,  step)
start_value means from where it should start iterating(included),end_value means till where it should iterate(excluding)
and step means interval i.e after how many elements it should consider next element.
Default is 1 i.e it should consider every element.step = 2 means consider 1 then skip 1, again consider 1 and so on.
For example :-
----------------------------
for i in range(1, 11, 2):
    print(i)"
----------------------------
will print 1, 3, 5, 7, 9 in the console.
Since it will iterate from 1 to 10 and will skip 1 element in between even iteration.
"""
# Simple example of list comprehension :- To create a list of double value of even numbers in range 1-10.
# Without list comprehension
even_double_list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        even_double_list1.append(i * 2)
print(even_double_list1)

# With list comprehension
even_double_list2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(even_double_list2)

# Few more examples of list comprehension
my_set = {2, 5, 7, 11, 12}
square_list = [i * i for i in my_set]
print(square_list)

sentence = "We are learning list comprehension"
sentence_constants = [i for i in sentence if i not in 'aeiou' and i != " "]
print(sentence_constants)

# Nested list comprehension :-
# Ex :- Create a list of tables.
table_list = [[k1 * k2 for k2 in range(1, 11)] for k1 in range(1, 11)]
print(table_list)

"""
Set comprehension and Dictionary comprehension :-
Like list comprehension, set comprehension and dictionary comprehension also exist.
They works similar to list comprehension.
"""

# Set comprehension example
triple_set = {i * 3 for i in range(1, 11)}
print(triple_set)
print(type(triple_set))

# Dictionary comprehension exampple
triple_cube_dictionary = {i: i * i * 3 for i in range(1, 6)}
print(triple_cube_dictionary)
print(type(triple_cube_dictionary))

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

old_dict = {k: v for (k, v) in original_dict.items() if v > 40}
print(old_dict)

# Nested dictionary comprehension
# Ex1 :- create a dictionary, where key represents numbers in range (11-15)
# and value is another dictionary of representing their multiplication with numbers in range (1-1)
nested_dict = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(11, 16)
}
print(nested_dict)

# Ex1 : create a dictionary, where key represents numbers in range (11-20)
# and value is another dictionary of representing square and cube of that number
square_cube_dict = {i: {f'{i} square': i * i, f'{i} cube': i * i * i} for i in range(11, 21)}
print(square_cube_dict)

# Combination of different type of comprehensions :
"""
Ex :- Combination of dictionary comprehension and list comprehension
To create a dictionary where key is range of 10 numbers like (1-10),(11-20) etc
and value is list of prime number in that range.
In this program we have declared and used a function.It is very basic kind of function which you can easily understand
We will learn about functions in details later
"""


def check_prime(num):
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for n in range(2, (math.floor(num / 2) + 1)):
            if num % n == 0:
                is_prime = False
                break
    return is_prime


prime_list_dict = {f'({k1 - 10} - {k1})': [k2 for k2 in range(k1 - 10, k1 + 1) if check_prime(k2)] for k1
                   in range(10, 101, 10)}
print(prime_list_dict)

# Similarly we can use any type of comprehensions in combinations
# like list of dictionaries, list of sets, set of dictionaries, dictionary of sets(i.e values as set) etc.
