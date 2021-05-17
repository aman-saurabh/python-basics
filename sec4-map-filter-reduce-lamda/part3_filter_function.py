"""
filter() function:
filter() function is used to filter out values for which a given condition is true.
Like map() function, the filter() function also takes two arguments - another function as first argument and an iterable as second one.
But in filter() function, the function which we pass as first argument must perform some test operation and return boolean value.
So filter() function is used to create an iterable consisting of values for which the function returns true.
Syntax of filter() function :
filter(function, iterables)

Other rules for function(which we pass as argument) and iterables, and returned iterables are same as in map() function.
"""
# Example1 :- To filter out numbers which are divisible of 3
num_tuple = (4, 16, 39, 57, 69, 71)
divisible_by_three = list(filter(lambda n: n%3 == 0, num_tuple))
print(divisible_by_three)

# Example2 :- To filter out employees whose salary is more than 100000
employees_details = [
    {"Aman": 120000},
    {"Mohan": 57000},
    {"Priyanka": 98000},
    {"Vineet": 150000},
    {"Michael": 107500}
]

highest_paid_employees = tuple(filter(lambda emp: list(emp.values())[0] > 100000, employees_details))
print(highest_paid_employees)

# Example 3:- To filter out dates which were earlier than 2010.
date_tuple = ("19 Jan, 2010", "14 march, 2012", "16 April, 2007", "28 August, 2009", "31 December, 2009")
early_dates = set(filter(lambda d: int(d.split(", ")[1]) < 2010, date_tuple))
print(early_dates)


