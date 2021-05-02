"""
In python there are basically two methods used for sorting of lists
1.) sort() method
2.) sorted() method
Both are quiet similar in the sense how they work.
The main difference between them is sort() method modifies the original list
while sorted() method stores the sorted data in a new list and doesn't modify the original list normally.
However if you want you can store the sorted data in the same list again and thus modify the original list.
"""

# 1.) ***** sort() method *****
# By default sort() method will sort the list alphanumerically(in case of strings)
# and in ascending order (in case of numbers)
# Example with default settings :-
# For strings :- alphanumeric sorting
my_list = ["Aman", "Manish", "16Pawan", "21Mohan", "3Pawan", "Deepak", "Amit21"]
my_list.sort()
print(my_list)

# For numbers :- ascending order
my_num_list = [21, 63, 9, 37, 5, 49]
my_num_list.sort()
print(my_num_list)

# sort() methods parameters :-
# sort() method supports two optional parameters -> reverse = True and key = function
# so the complete syntax of sort() method is as follows -> list_name.sort(reverse = True, key = function)


# 1.) reverse = True
# This is used to sort list in opposite of default sorting
# i.e to sort list in reverse of alphanumeric order(in case of strings) and in descending order(in case of numbers)
# Ex :- Same previous example but this time with parameter 'reverse = True'
my_list = ["Aman", "Manish", "16Pawan", "21Mohan", "3Pawan", "Deepak", "Amit21"]
my_list.sort(reverse=True)
print(my_list)

# 2.) key = function
# This parameter is used to specify the method that should be used for custom sorting.
# For example for sorting a list of strings based on their length.we can pass "key = len()" method.
names = ["Joe", "Amy", "Saurabh", "Neha", "Michael", "Aman", "Mukul", "Pritam"]
names.sort(key=len)
print(names)
# Here one thing you must note that we have used method name only i.e 'len' in this case.
# We haven't actually called the method i.e by using parenthesis.
# For 'key' parameter you must provide the reference of the function only and should not call that method.

# Custom functions for sorting :-
# We can use custom functions also for sorting as we used len() function in previous example
# Sort the list of numbers based on how close the number is to 50
num_list = [53, 48, 65, 37, 23, 71]


def distance_with_fifty(num):
    return abs(num - 50)


num_list.sort(key=distance_with_fifty)
print(num_list)


# Ex 2: Sort the list of tuples according to descending order of the last element of the tuple
def get_second(my_tuple):
    return my_tuple[len(my_tuple) - 1]


tuple_list = [(2, 2), (3, 5, 2), (5, 7, 1), (5, 7, 5), (5, 7, 3, 4)]
tuple_list.sort(reverse=True, key=get_second)
print(tuple_list)

# 2.) ***** sorted method *****
# As discussed earlier sorted() method is similar to sort() method.However their syntax is little different.
# Complete syntax of sorted() method is -> "sorted(list_name, reverse=True, key=function)"
# Simple example of sorted() method
my_num_list1 = [21, 63, 9, 37, 5, 49]
sorted(my_num_list1)
print(my_num_list1)

# But the main difference between them is that sort() method modify the original list
# while sorted method doesn't modify the original list normally,
# instead simply returns the sorted list which you can store in a new list
# or in the same original list if you want to modify that.
# So in previous example if we use sorted() method inplace of sort() method.
# Then you will find list is not sorted.
tuple_list = [(2, 2), (3, 5, 2), (5, 7, 1), (5, 7, 5), (5, 7, 3, 4)]
sorted(tuple_list, reverse=True, key=get_second)
print(tuple_list)
# Here actually list is sorted but it didn't modify the original list.Instead it would have returned sorted list
# But we didn't catched the value in any variable, so the sorted list is lost.
# We can catch the value as follows :-
# 1.) If we want the values in a new list, so that original list don't gets disturbed.
new_tuple_list = sorted(tuple_list, reverse=True, key=get_second)
print(new_tuple_list)

# 2.) If we want the values in the same list i.e if we want to modify the original list
tuple_list = sorted(tuple_list, reverse=True, key=get_second)
print(tuple_list)
