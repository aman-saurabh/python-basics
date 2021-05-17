# Program to use map() and filter() functions in reduce() function.
# Example :-
# Write a program to get sum of cube of even numbers from the given list of numbers.
from functools import reduce

num_list = [4, 7, 9, 12, 15, 18]
cube_even_numbers = reduce(lambda x, y: x + y, map(lambda a: a ** 3, filter(lambda n: n % 2 == 0, num_list)))
print(cube_even_numbers)

