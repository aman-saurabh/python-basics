"""
As we know that map() function and filter() functions requires an iterable as second argument
and they also returns an iterable. So we can pass any of them as the second element into other function.
For example we can pass a map() function into other map() function or a map() function into a filter() function etc.
Even we can pass a map() or filter() function as second element in reduce function also
as it also require an iterable as second argument. But since reduce() function don't return an iterable,
so we can't pass them as second argument into a map() or filter() function,
even we can't pass them as second argument into some other reduce() function also.
In this part we will see how to use map() and filter() in combination.
In next part we will see how to use reduce() in combination with map() and filter()
"""
# Example1 :- filter() within map()
# Write a program to get square of all numbers in the given list, which are divisible by 3.
num_list = [4, 6, 9, 12, 13]
three_divisible_square = list(map(lambda a: a**2, filter(lambda x: x % 3 == 0, num_list)))
print(three_divisible_square)

# Example2 :- map() within filter()
# Write a program to get the list of reverse of words from the given list of words, whose reverse starts with vowels.
words = ("Aman", "Pumpkin", "Ape", "Mango", "Lion", "Apple")
filtered_words = list(filter(lambda a: a.lower()[0] in ['a', 'e', 'i', 'o', 'u'],
                             map(lambda s: s.lower()[::-1].capitalize(), words)))
print(filtered_words)
