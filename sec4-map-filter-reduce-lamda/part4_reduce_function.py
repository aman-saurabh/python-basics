"""
reduce() function :-
reduce() works differently than map() and filter(). It does not return a new iterator based on the function and iterable we've passed. Instead, it returns a single value.

Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.

reduce() works by calling the function we passed for the first two items in the sequence first. The result returned by that function call is used in another call to the function alongwith with the next element (i.e third element). This process repeats until we've gone through all the elements in the given iterable.

It also accepts an optional argument 'initial' which when passed, it works as the initial value i.e in such cases, in first funcion call, first two elements of the given iterable are not passed as arguments instead the 'initial' value and the first element of the given iterable are passed. In this way, the 'initial' value, when provided, works as the 0th element of the given iterable i.e before the first element of the given iterable.
Syntax of reduce() function :-
filter(function, iterables, [initial])
# Here we has used square brackets for initial to indicate that it is optional argument.
"""
# Example1 :- To get the sum of all elements in the given list
from functools import reduce

num_list = [3, 5, 8, 9, 10]
print("With an initial value: " + str(reduce(lambda x, y: x + y, num_list)))
print("With an initial value: " + str(reduce(lambda x, y: x + y, num_list, 10)))
# Note :- Here 10 is the value for 'initial'.

# Example2 :-
monthly_expense = [
    {"rent": 15000},
    {"dairy": 5500},
    {"grocery": 10000},
    {"dine-out": 3000},
    {"shopping": 12000}
]
x = dict()
total_expense = reduce(lambda a, b: {"total": (list(a.values())[0] + list(b.values())[0])}, monthly_expense)
"""
Here we are returning a dictionary from the lambda function as the given iterable items are list.
So if we don't return values as dictionary and instead if we simply return the sum as simply 'int' value 
then in the second function call the function will get first argument as int value 
and the second argument as 'dictionary'.And thus it will lead to error.
"""
print("Total monthly expenses : ", total_expense.get('total'))
