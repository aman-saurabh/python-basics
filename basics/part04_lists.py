"""
Lists are ordered, mutable collection of elements.They are similar to arrays of other languages.
Lists are created using square brackets.
A list can contain duplicate items.
Since like strings list are also ordered, so concept of index and slicing is there in lists also.
Unlike trings, lists are mutable i.e we can change add or remove items in a lsit after it has been created.
"""

animals = ["Lion", "Tiger", "Elephant", "Dear", "Bear", "Monkey", "Ape", "Giraffe", "Fox", "Leopard"]
print(animals[0])
# Lion
print(animals[2])
# Elephant
print(animals[-2])
# Fox
print(animals[:9])
# ['Lion', 'Tiger', 'Elephant', 'Dear', 'Bear', 'Monkey', 'Ape', 'Giraffe', 'Fox']
print(animals[2:9])
# ['Elephant', 'Dear', 'Bear', 'Monkey', 'Ape', 'Giraffe', 'Fox']
print(animals[-9:-3])
# ['Tiger', 'Elephant', 'Dear', 'Bear', 'Monkey', 'Ape']
print(animals[9:2:3])
# [] -> Since in case of positive z, x should be less than y
print(animals[2:9:3])
# ['Elephant', 'Monkey', 'Fox']
print(animals[2:9:-3])
# [] -> Since in case of negative z, x should be greater than y
print(animals[9:2:-3])
# ['Leopard', 'Ape', 'Dear']
print(animals[-9:-2:-3])
# [] -> Since in case of negative z, x should be greater than y
print(animals[-2:-9:-3])
# ['Fox', 'Monkey', 'Elephant']


# ***** Change list items *****
animals[1] = "Zebra"
# Tiger will be replaced by Zebra
print(animals)
animals[-2] = "Wolf"
# Fox will be replaced by Wolf
print(animals)
# Change a range of items
animals[2:5] = ['Hippopotamus', 'Wolf']
print(animals)
# Note that here we have removed 3 items while inserted only 2 items.
# So it is not necessary that we should replace with same number of items.
# Here also note that we have inserted Wolf again even though it is already there in the animals list.
# And even you can check in the result that Wolf is present two times, which shows duplicate items are allowed in List.

# ***** Add list items *****
students = ["Aman", "Manish", "Vipul", "Sohan"]
print(students)
# 1. append() method : Add item to the end of the list.
students.append("Neha")
print(students)

# 2. insert() method : Insert item at a specified index
students.insert(2, "Swati")
print(students)

# 3. extend() method: To append items from any kind of iterable like list, set, tuples etc. to the current list.
guest_student_list = ["Pradeep", "Vivek"]
guest_student_tuple = {"Nitin", "Farha"}
students.extend(guest_student_list)
print(students)
students.extend(guest_student_tuple)
print(students)

# ***** Remove list items *****
# 1. remove() method: Remove a specified item
students.remove("Nitin")
print(students)

# 2. pop() method :- Remove an item with specified index
students.pop(3)
print(students)
# Note :- In pop() method we can omit specifying index.In such cases it will remove last item
students.pop()
print(students)

# 3. del() keyword :- Delete specified items from a list (items are specified using their index as in string slicing)
del students[1]
print(students)
del students[2:5]
print(students)
# Note :- 'del' keyword can be used to delete entire list also.For that simply don't specify the index
del students
# print(students)
# Now above line will throw error.Since now 'students' list is deleted and it does not exist now.

# defining 'students' list again since we had deleted earlier
students = ["Aman", "Mohan", "pankaj"]
print(students)
# 4. clear() method :-
students.clear()
print(students)

# ***** Copy list *****
# 1.) copy() method :- Returns the copy of the list.
animals_copy = animals.copy()
print(animals_copy)

# 2.) list() constructor :-
new_animals_list = list(animals)
print(new_animals_list)

# ***** Joining two or more lists *****
# 1.) using '+' operator :- To create a new list by joining several lists. It doesn't modify existing lists normally.
# However you can modify any existing list also by catching the result in some existing list instead of a new one.
# i.e in the following example if you want all value in list1 itself then replace line 3 as : "list1 = list1 + list2"
list1 = ["one", "two", "three"]
list2 = ["four", "five", "six"]
list3 = list1 + list2
print(list3)

# 2.) using extend method :-
# Note :- extend() method is mainly used to copy all items of one list to another list


# ***** Few other important methods and keywords *****
# Intentionally printing animals here just to see what is present in it at this stage.
print(animals)
# 1.) len() method :- Returns the number of elements present in the list
print(len(animals))

# 2.) count() method :- Returns the number of number of times a specified item is present in the list.
print(animals.count("Wolf"))

# 3.) index() method :- Returns the index of the first occurrence of item in the list.
# If the item is not present it
print(animals.index("Wolf"))
# complete syntax of index() method is - list.index(item, start_index, end_index).
# start_index and end_index are optional parameters, used to specify the range in which item should be searched.
# start_index is included while end_index is excluded in the search.And we can't specify end_index with start_index.
print(animals.index('Wolf', 4))

print(animals.index('Wolf', 4, 8))
# print(animals.index('Cow'))
# Note that in case if the item is not present, which you specified in index method, it will throw error.

# 4.) reverse() method :- Reverses the order of elements present in the list i.e first item become last and so on.
print(animals)
animals.reverse()
print(animals)

