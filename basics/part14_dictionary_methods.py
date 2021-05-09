# Dictionary to be used in following methods :
my_dict = {"name": "Aman", "age": 30, "city": "Noida", "type": "customer"}

# 1.) clear() method :-
# Removes all items from the dictionary.Example :
# Creating a copy of 'my_dict' to use in following example.So that original 'my_dict' don't get updated.
my_dict_copy1 = my_dict.copy()

print(my_dict_copy1)
my_dict_copy1.clear()
print(my_dict_copy1)

# 2.) fromKeys() method :-
# Returns a dictionary with specified keys and values
# Keys can be any iterable like tuple, list, set, string, etc.
# And each item of the given iterable will be added as key in the dictionary
# Here values can also be anything(like list, number, set, dictionary etc) but it will consider value as a single unit
# and will assign that value to each and every key
# For example :
a = ("num1", "num2", "num3")
b = 21
c = [12, 35, 24, 9]
d = "Aman"

x = dict.fromkeys(a, b)
print(x)

y = dict.fromkeys(a, c)
print(y)

z = dict.fromkeys(d, b)
print(z)

# 3.) pop() method :-
# pop() method removes the item with specified key and also return its value.
# Note :- In pop() method 'key' is important. If you don't pass a 'key' as argument then it will throw error.
# And even if you pass a key and if the key is not present in the dictionary then also it will throw error.
# But there is a workaround to solve this problem.Actually pop() method accept two arguments -
# 1.) key -> The key of item which you want to remove
# 2.) default_value -> The value which it should return in case key is not found in the dictionary.
# So by passing second parameter(i.e default_value) we can avoid error in case of non-existing keys.
# Example :
# Creating a copy of 'my_dict' to use in following example.So that original 'my_dict' don't get updated.
my_dict_copy2 = dict(my_dict)
# Without default_value - Should be used if you are sure that the key exist
v1 = my_dict_copy2.pop('city')
print(v1)
# With default_value - Should be used if you are not sure that the key exist or not
v2 = my_dict_copy2.pop('designation', 'NotExist')
print(v2)

# 4.) popitem() method :-
# Removes the last inserted item(i.e key-value pair) and also return the same
z = my_dict_copy2.popitem()
print(z)
print(my_dict_copy2)

# 5.) setdefault() method :-
# Complete syntax of setdefault() method :-
# dictionary_object.setdefault(key, default_value)
# Here key is required argument while default_value is optional and its default value is 'None'.
# setdefault() method returns the value of specified key
# And if the key is not already present then it insert the key with given default value
# or 'None' in case default_value is not provided as a new item to the dictionary and also returns default_value.
# Example :
# In case key already exist
p = my_dict.setdefault("name", "Manish")
print(p)
print(my_dict)

# In case key does not exist and we have provided default_value
q = my_dict.setdefault("nationality", "Indian")
print(q)
print(my_dict)

# In case key does not exist and we haven't provided default_value
r = my_dict.setdefault("company")
print(r)
print(my_dict)
