"""
Sets are unordered collection of unique and hashable objects.
Unordered means, in sets items doesn't have a fixed index,
and unique means duplicate objects are not allowed in sets,
Sets are written with curly brackets.
Hashable :-
An object is said to be hashable if it has a hash value that remains the same during its lifetime.
So every hashable object has a __hash__() method using which we can get the hash value of that object.
For example :-
my_name = "Aman"
your_name = "Mohan"
print(hash(my_name))        # O/P : 1182558986998896388 (Value will be different.Just see the format.Can be -ve as well)
print(my_name.__hash__())   # We can use any of these two methods
This hash value is used to compare objects. For this, it needs the __eq__() or __cmp__() methods.
If hashable objects are equal when compared, it means they have the same hash value.
print(my_name.__eq__(my_name))          # True
print(my_name.__eq__(your_name))        # False

Being hashable an object is usable as a dictionary key and a set member
as these data structures use hash values internally.
All immutable built-in objects in python are hashable.
Mutable containers like lists and dictionaries are not hashable while immutable container tuple is hashable.
So a set and dictionary-key can contain a tuple but not lists or dictionaries.
Objects which are instances of user-defined classes are also hashable by default.
"""
# Examples of hashable objects :-
my_str = "Aman"
print(hash(my_str))
my_num = 57.5
print(my_num.__hash__())
my_tuple = (1, "Aman", True)
print(hash(my_tuple))
# my_list = [1, "Aman", True]
# Above line will throw error.Since lists are mutable and hence not hashable

# Now let's discuss about sets.
# Set Example :-
my_set = {"Aman", "Mohan", "Pawan", "Vinay", "Aman", "Pankaj", "Sapna", "Samir"}
print(my_set)
"""
While defining 'my_set' we have entered 'Aman' two times.But when you print this set you will see :
'Aman' is printed only once i.e only one 'Aman' is inserted into 'my_set' and another one was ignored.
It is because sets does not allow duplicate values.
you can also see that items are not printed in the order in which they were inserted.
It is because sets are unordered. And in sets an item does not have a fixed index. 
"""

# Accessing set items :-
"""
As we learned earlier, in sets, items does not have a fixed index, so we can't access set items using their index.
But we can loop through set items using for loop.
But please note that we can loop through set items using simple for loop only
and not through for loop with range() and len() functions and nor through while loop.
"""
# Ex :- Loop through set items(Only way to  access set items)
for item in my_set:
    print(item)

# How to check if an item is present in a set or not
# We can check if an item is present in a set or not using "in" operator as follows :
print("Aman" in my_set)         # Will print 'True'.Since Aman is present in my_set.
print("Vikram" in my_set)       # Will print 'False'.Since Vikram is not present in my_set.

# Modify set items :-
# Once set is created we can't change set item, but we can add or remove items from a set.

# 1.) Add items to a set :-
# a.) Using add() method :-
my_set.add("Manish")
print(my_set)

# b.) Using update() method :-
# update() method is used to add items from an iterable(like list,tuple,string,range() function etc) to the current set.
my_new_set = {"Mike", "John", "Joe", "Patrick"}
my_list = ["One", "Two"]
my_range = range(5)
my_string = "Mohan"
my_new_set.update(my_list)
my_new_set.update(my_range)
my_new_set.update(my_string)
my_new_set.update(my_set)
print(my_new_set)

# 2.) Remove items from a set :-
# a.) By using remove() method :-
my_new_set.remove("Patrick")
print(my_new_set)
# Following line will throw error since "Vijaya" is not present in my_new_set.
# my_new_set.remove("Vijaya")

# b.) By using discard() method :-
my_new_set.discard("M")
print(my_new_set)
# Following line will not throw error even though "Vijaya" is not present in my_new_set.Actually it will do nothing.
my_new_set.discard("Vijaya")
print(my_new_set)

# So the difference between remove() and discard() method is remove() methods will throw error if item is not present.
# While discard method won't.It will simply ignore the command.

# c.) By using pop() method :-
"""
Generally, in Python, pop() method is used to remove one item from the last but in sets, since items are unordered,
So we can't guess which item will be removed. So if you need to remove any one item from a set randomly 
or all items one by one, then only you should go for pop() method.
Another point to be noted here is, pop() method also returns the item it removes.
And if there is no item remaining in the set and if you call pop() method, then it will throw error.   
"""
print(my_new_set.pop())
print("After calling pop() method 1st time : "+str(my_new_set))
print(my_new_set.pop())
print("After calling pop() method 2nd time : "+str(my_new_set))

# Other set methods :-
# 1.) copy() method :- Return a copy of the set.
my_set_copy = my_set.copy()
print(my_set_copy)

# 2.) clear() method :- Removes all items from the set
my_set_copy.clear()
print(my_set_copy)

# 3.) isdisjoint() method :- Returns whether two sets are disjoint sets or not.
# Two or more sets are said to be 'disjoint' sets if they don't have any common item.
print(my_new_set)
print(my_set)
print(my_set.isdisjoint(my_new_set))

# 4.) issubset() :- Returns whether the second set contains all items of first set or not
print(my_set.issubset(my_new_set))
# Here we are checking if 'my_set' is a subset of 'my_new_set' or not
# i.e whether 'my_new_set' contains all items of 'my_set' or not.

# 5.) issuperset() :- Returns whether the first set contains all items of second set or not
print(my_set.issuperset(my_new_set))
# Here we are checking if 'my_new_set' is a superset of 'my_set' or not
# i.e whether 'my_set' contains all items of 'my_new_set' or not.
# i.e it is opposite of 'issubset' method.
