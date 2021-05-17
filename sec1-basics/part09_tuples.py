"""
Tuples are ordered immutable sequence of objects.
Ordered means every item in Tuple has some fixed index and immutable means tuples are unchangeable
i.e we can't add, remove, or change items from the tuple once they are created.
Duplicate objects are allowed in Tuples and Tuples are written with round brackets(i.e parenthesis).
Note :- If a tuple has only one item then always put a comma in the end,
otherwise python will not consider that as tuple,it will be considered as a string.
"""

first_tuple = ("Lion")
# Since only one item and without comma in the end so python will consider it as string not tuple
print(type(first_tuple))
second_tuple = ("Lion",)
# Since only one item but with comma in the end so python will consider it as tuple and not string
print(type(second_tuple))
# In case of multiple item, whether we give comma at the end or not, in both cases python will consider it as tuple.
# But to compliance with the rule made for single item, we should always give comma in the end in tuples.
# So that we become habitual to that and never fails in case of single item.
third_tuple = ("Lion", "Tiger", "Leopard",)
print(type(third_tuple))

# Accessing tuple items :-
# Since like lists, tuples are also ordered collection of objects hence every item of a tuple has some fixed index.
# And therefore Slicing concept works for tuples as well
my_tuple = ("Aman", "Mohan", "Pawan", "Vinay", "Aman", "Pankaj", "Sapna", "Samir")
print(my_tuple[2])
print(my_tuple[2:7])
print(my_tuple[-7:-2])
print(my_tuple[7:2:-1])
print(my_tuple[2:7:-1])  # Will not produce any result, as in case of negative z, x should be greater than y
print(my_tuple[7:2:-2])
print(my_tuple[-7:-2:-2])  # Will not produce any result, as in case of negative z, x should be greater than y
print(my_tuple[-2:-7:-2])

# Update tuples :- Add, remove or replace tuple items
# Since tuples are immutable. Hence we can't add, remove or replace items to a tuple.

# Unpacking of tuples :-
# When we create a tuple we normally assign value to it.This is called packing of a tuple.
# Ex :-
fruit_tuple = ("Apple", "Papaya", "Mango")
# But in python its reverse is also possible,
# i.e in python we can extract values of a tuple back into variables in the same manner.
# This is called unpacking of tuples.For example :
(green_fruit, yellow_fruit, red_fruit) = fruit_tuple
print("Green color fruit : " + green_fruit)
# It will print 'Apple'.Since 'Apple' was at index 0 and we extracted first item in variable 'green_fruit'.
print("Yellow color fruit : " + yellow_fruit)
# It will print 'Papaya'.Since 'Papaya' was at index 1 and we extracted second item in variable 'yellow_fruit'.
print("Red color fruit : " + red_fruit)
# It will print 'Mango'.Since 'Mango' was at index 2 and we extracted third item in variable 'red_fruit'.
"""
Note :-
In unpacking of tuple, number of variables on left-hand side should be equal to number of values in given tuple.
If they are not equal i.e if the number of variables is greater than or less than the number of values in given tuple
Then in such cases, it will throw error.
However python provides a special syntax(*args) to store all remaining values in a single variable while unpacking tuple
This special syntax (i.e '*args') must be used in case the number of variables is less than the number of values.
And it must be used as the last variable in left-hand side.
In such cases every variable on the left-hand side to '*args' will a assigned a corresponding value
and remaining values will be assigned to '*args'.
Here one thing must be noted that, we are using '*args' to refer the syntax.It is not necessary that we use '*args' only
We can use any variable name with this syntax for this purpose like - '*rest', '*remaining', '*all' etc.
"""
# Another example of tuple unpacking with '*args' :-
# In this example we will use same "my_tuple" tuple which we created in the first example.
(first, second, third, fourth, fifth, *rest) = my_tuple
print("my_tuple length : " + str(len(my_tuple)))
print("First : " + first)
print("Second : " + second)
print("Third : " + third)
print("Fourth : " + fourth)
print("Fifth : " + fifth)
print("Remaining : " + str(rest))

# Tuple constructor :-
# tuple constructor is used to create a tuple from some existing iterable like list, set, string, range() function etc.
emp_list = ["Aman", "Samir", "Manish", "Sachin", "Punit"]
emp_tuple = tuple(emp_list)
range_tuple = tuple(range(1, 10))
print(range_tuple)
my_string = "My name is Aman"
str_tuple = tuple(my_string)
print(str_tuple)

# Join tuples :-
# We can join two or more tuples using '+' operator as follows :
one_digit_tuple = (1, 2, 3)
two_digit_tuple = (11, 12, 13)
three_digit_tuple = (101, 102, 103)
number_tuple = one_digit_tuple + two_digit_tuple + three_digit_tuple
print(number_tuple)


# Tuple methods :-
# Defining a tuple to use in following methods :-
name_tuple = ("Sunny", "Binny", "Sunny", "Ginny", "Munny")
# 1.) count() method :- Returns the number of times the specified element is present in the tuple
# Ex :-
print(name_tuple.count('Sunny'))

# 2.) index() method :- Returns the index of first occurrence of an element present in the tuple.
print(name_tuple.index('Sunny'))
# complete syntax of index() method is - list.index(item, start_index, end_index).
# start_index and end_index are optional parameters, used to specify the range in which item should be searched.
# start_index is included while end_index is excluded in the search.And we can't specify end_index with start_index.
print(name_tuple.index('Sunny', 1, 4))
# It will return 2, since in this case it will start searching from index 1.
# Note that in case if the item is not present, which you specified in index method, it will throw error.
