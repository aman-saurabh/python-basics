"""
i.) map() function :-
map() function is used to perform same operation on each element of a given iterable.
The map() function takes two arguments - another function as first argument and an iterable as second one
and it returns an iterable as output after applying the function to each element of the given iterable.
i.e it returns an iterable with same number of elements as the given iterable.
Syntax of map() function :-
map(function, iterables)

As discussed in previous part. We can pass a normal user-defined functions as well as a lambda function
(if it contains a single expression) in map() function as first argument.
And we can pass any iterable with any number of elements in that as second argument.
Here also note that we should pass only the function name as first argument and we should not call it.
"""
# Example1 :- To get square of all given numbers.
num_list = [1, 2, 3, 4, 5]


# With normal function :-
def get_square(num):
    return num * 2


squares_function = map(get_square, num_list)
print(squares_function)
# With lambda function :-
squares_lambda = map(lambda x: x * 2, num_list)
print(squares_lambda)
"""
Here as we will see that it returns the memory location of the output and not the actual values.
But as we know that map returns an iterable
so we can get values either using for loop or using list, set, tuple etc. constructors.
Here note that if you use 'set' constructors then it will return values in a set, 
hence in such cases, you might miss duplicate values if two or more items of given iterable produces same result,
and even the values will also not be in same order as the given iterable, So until necessary, never use set constructor
Also note that you can run loop or use list, set, tuple etc. constructors only once for any map() function.
Actually while producing values, it flushes out the values it holds, So next time when you try it returns nothing.  
"""
for item in squares_function:
    print(item)

square_list = list(squares_lambda)
print(square_list)
"""
To get result in following code, comment out above codes, otherwise it will produce empty results.
As we can get values from a map() function only once, either using loop or using list, set, tuple etc. constructors.
And we have already done it above using 'for' loop for 'squares_function' and 'list constructor' for 'squares_lambda'.
"""
square_set = set(squares_function)
print(square_set)
square_tuple = list(squares_lambda)
print(square_tuple)

# Example2 :- To check whether the string starts with Vowel or Consonant.
str_list = ["Aman", "Guava", "Lion", "Apple", "Peacock", "Uttam"]
check_first_letter = list(map(lambda s:'Vowel' if s.lower()[0] in ['a', 'e', 'i', 'o', 'u'] else 'Consonant', str_list))
print(check_first_letter)

# Example3 :- To get the area for circles with given radius.
radius_tuple = [5, 3.6, 6.57, 3]
area_of_circles = tuple(map(lambda r: round(3.14 * r ** 2, 2), radius_tuple))
# round() function is used to round up values up to 2 decimal places.
print(area_of_circles)
