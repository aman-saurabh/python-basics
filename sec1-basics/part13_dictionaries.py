"""
Dictionaries are unordered, mutable collection of objects where data is stored in key-value pairs.
In dictionaries keys must be unique i.e they can't be duplicated while values can be duplicated.
Dictionaries are written with curly brackets like sets.
"""
# 1.) Example of a dictionary :-
car_dict = {
    "brand": "Tata",
    "model": "Safari",
    "year": 2021
}
print(car_dict)

# 2.) Accessing dictionary items :-
# Dictionary items can be accessed by using following two methods :
# i.) By using 'square' brackets :-
# Example :
print(car_dict['model'])

# ii.) By using get() method :-
# Example :
print(car_dict.get('year'))

# 3.) How to get all keys and all values of a dictionary :-
# i.) To get all keys -> keys() method :-
car_dict_keys = car_dict.keys()
print(car_dict_keys)

# ii.) To get all values -> values() method :-
car_dict_values = car_dict.values()
print(car_dict_values)

# Data of keys() and values() methods looks like as if they are of 'list' type but actually they are not.
# So we can't apply methods of 'list' to them and we can't access their item using index, but we can run loop on them
# However they are not list but they looks like list, hence we call them as 'keys-list' and 'values-list' respectively.
# Checking type of response of keys() and values() method.
print(type(car_dict_keys))              # It will print <class 'dict_keys'> and not <class 'list'>
print(type(car_dict_values))            # It will print <class 'dict_values'> and not <class 'list'>

# Accessing keys items using index - Will throw error, since we can't access items using index and hence commented.
# print(car_dict_values[0])

# Running loop on values - similarly we can run loop on keys also.
for x in car_dict_values:
    print(x)

# Note :- Any changes done in the dictionary will be reflected in the 'keys-list' and 'values-list' also.
# Ex : We have already stored keys-list and values-list in 'car_dict_keys' and 'car_dict_values' variables respectively.
# Now if we modify the dictionary by adding a new key-value pair or by updating any key's value.
# And then if we simply print 'car_dict_keys' and 'car_dict_values'.Then we will see updated values are also printed.
# It asserts that if we modify the dictionary, its keys-list and values-list also gets modified.

# Updating existing key's value
car_dict['model'] = 'Sierra'
# Adding a new key value pair
car_dict['color'] = 'White'
# Printing keys-list and values-lists
print(car_dict_keys)
print(car_dict_values)

# 4.) Add item or update item in a dictionary :-
# We can add or update items in a dictionary using following two methods.
# In both methods if the key already exist, then it will update the value and if the key does not exist
# then it will add the key-value pair as new item.

# i.) By using square brackets :
# We have already seen its example in previous section.Let's see another one
# Updating item
car_dict['model'] = 'Nixon'
# Adding new item
car_dict['fuel'] = 'Electric'

# ii.) By using 'update()' method :-
car_dict.update({"color": "Blue"})
# Adding new item
car_dict.update({'transmission': 'Manual'})
print(car_dict)

# 5.) Loop through a dictionary :-
# i.) Using normal 'for' loop :-
for item in car_dict:
    print(item)                 # Will print key
    print(car_dict[item])       # Will print value
    print("------------")       # Just for separation

# just for separation between results of above and below loops
print("***********")

# ii.) Using 'for' loop with items() method of dictionary :-
for k, v in car_dict.items():
    print(k)                    # Will print key
    print(v)                    # Will print value
    print("------------")       # Just for separation

# 6.) Copy dictionaries :-
# We can copy a dictionary simply by assigning the dictionary into a new variable.
# For example - Suppose we have a dictionary named 'original_dictionary' and we want to copy this dictionary.
# We can copy this dictionary into a new variable let's say 'copy_dictionary' as follows :
# copy_dictionary = original_dictionary
# This rule is true not only for dictionaries, but for almost everything like lists, sets, tuples, strings etc.
# Apart from above method, we can use following methods of dictionary to copy a dictionary :

# i.) Using 'copy()' method :-
car_dict_copy1 = car_dict.copy()
print(car_dict_copy1)

# ii) Using dict() constructor :-
car_dict_copy2 = dict(car_dict)
print(car_dict_copy2)

# 7.) Nested Dictionaries :-
# A dictionary can have another dictionary within it as an item. Such dictionaries are callled nested dictionaries.
# Example:
employee_profile = {
    "name": "Aman Saurabh",
    "age": 30,
    "designation": "Senior developer",
    "address": {
        "addr": "HM Street",
        "city": "Noida",
        "pin": 201301
    }
}
print(employee_profile)
