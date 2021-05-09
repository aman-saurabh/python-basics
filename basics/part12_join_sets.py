"""
Two or more sets can be joined together using following methods :
But before we start learning about these methods, let's look at some points related to that :
1.) These methods can be used to add not only two or more sets, but also any iterable to a set like
    list, tuple, etc.
2.) Here joining means not to copy all items from one set and paste in another one.
    Here Actually every method has its own meaning of joining.
3.) Here we will list methods in pairs.Both methods of the pair are almost same.
    The only difference between the first method and second method of the pair is :
    The first method will join given sets and will return the resulting data as a new set
    so you have to catch the result in a new set or in any existing set if you want to modify that set.
    Otherwise data will be lost.
    while the second method (usually name includes 'update') will update the first set itself and won't return anything.
"""

# Sets to be used in all methods :
x = {"Apple", "Banana", "Cherry"}
y = {"Google", "microsoft", "Apple"}

# 1.) union() and update() method :
# a.) union() method :-
# This method will copy all items of both sets and will return all those items in the form of a set.
# So you have to catch the result in a new set or in any existing set if you want to modify the existing one.
# Otherwise data will be lost.
new_set1 = x.union(y)
print(new_set1)                         # Will print all items of both sets
print(x)                                # Same as earlier
print(y)                                # Same as earlier

# b.) update() method :-
# Same as 'union' method.But this method don't return anything instead it will update the first set itself.
# Creating z1 to use as first set in following example, so that our x and y don't get modified.
z1 = x.copy()
new_set2 = z1.update(y)                 # Here catching the result is useless.As it won't return anything.
print(new_set2)                         # Will print 'None' as 'update' method don't return anything.
print(z1)                               # Should be modified and now it should contain all items from both sets.


# 2.) intersection() and intersection_update() method :-
# a.) intersection() method :-
# This method will copy only all common items of both sets and will return all those items in the form of a set.
# So you have to catch the result in a new set or in any existing set if you want to modify the existing one.
# Otherwise data will be lost.
new_set3 = x.intersection(y)
print(new_set3)                         # Will print all common items of both sets
print(x)                                # Same as earlier
print(y)                                # Same as earlier

# b.) intersection_update() method :-
# Same as 'intersection' method.But this method don't return anything instead it will update the first set itself.
# Creating z2 to use as first set in following example, so that our x and y don't get modified.
z2 = x.copy()
new_set4 = z2.intersection_update(y)    # Here catching the result is useless.As it won't return anything.
print(new_set4)                         # Will print 'None' as 'intersection_update' method don't return anything.
print(z2)                               # Should be modified and now it should contain all common items from both sets.


# 3.) symmetric_difference() and symmetric_difference_update() method :-
# a.) symmetric_difference() method :-
# This method will copy only all uncommon items of both sets and will return all those items in the form of a set.
# So you have to catch the result in a new set or in any existing set if you want to modify the existing one.
# Otherwise data will be lost.
new_set5 = x.symmetric_difference(y)
print(new_set5)                         # Will print all uncommon items of both sets
print(x)                                # Same as earlier
print(y)                                # Same as earlier

# b.) symmetric_difference_update() method :-
# Same as 'symmetric_difference' method.
# But this method don't return anything instead it will update the first set itself.
# Creating z3 to use as first set in following example, so that our x and y don't get modified.
z3 = x.copy()
new_set6 = z3.symmetric_difference_update(y)        # Here catching the result is useless.As it won't return anything.
print(new_set6)                         # Will print 'None' as this method don't return anything.
print(z3)                               # Should be modified and now it should contain all common items from both sets.


# 4.) difference() and difference_update() method :-
# a.) difference() method :-
# This method will copy all items of first set except those which are present in second set also
# and will return all those items in the form of a set.
# So you have to catch the result in a new set or in any existing set if you want to modify the existing one.
# Otherwise data will be lost.
new_set7 = x.difference(y)
print(new_set7)                         # Will print all items of first set except those present in second set also.
print(x)                                # Same as earlier
print(y)                                # Same as earlier

# b.) difference_update() method :-
# Same as 'difference' method.
# But this method don't return anything instead it will update the first set itself.
# Creating z4 to use as first set in following example, so that our x and y don't get modified.
z4 = x.copy()
new_set8 = z4.difference_update(y)      # Here catching the result is useless.As it won't return anything.
print(new_set8)                         # Will print 'None' as this method don't return anything.
print(z4)                               # Should be modified and now it should contain all common items from both sets.

# Now let's see few example of how to use these methods with other iterables.
my_range = range(1, 6)
mixed_set1 = x.union(my_range)
print(mixed_set1)

my_tuple = ["Tomato", "Cucumber", "Apple"]
mixed_set2 = x.intersection(my_tuple)
print(mixed_set2)

my_list = ["Tomato", "Cucumber", "Apple"]
mixed_set3 = x.symmetric_difference(my_list)
print(mixed_set3)

mixed_set4 = x.difference(my_list)
print(mixed_set4)

