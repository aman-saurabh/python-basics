# Example1 :-
x = [[200, "Aman"], [120, "Monty"], [150, "Vineet"]]
for uid, name in x:
    print(f"Uid : {uid}, Name : {name}")
else:
    print("Unpacking of list of lists using for loop completed")

# Example2 :-
y = [(200, "Aman"), (120, "Monty"), (150, "Saurabh")]
count = 0
while count < len(y):
    uid, name = y[count]
    print(f"Uid : {uid}, Name : {name}")
    count += 1
else:
    print("Unpacking of list of tuples using while loop completed")

# Example3 :-
z = {(200, "Aman"), (120, "Monty"), (150, "Saurabh")}
for uid, name in z:
    print(f"Uid : {uid}, Name : {name}")
else:
    print("Unpacking of set of tuples using while loop completed")

"""
Notes :- 
1.) We shouldn't unpack iterables containing sets(i.e set as inner iterable) in this way as sets are unordered
    so there are chances that items will be interchanged in the result. 
    i.e in the above examples if we use "set" as inner iterable then there are chances that 
    at some places we will get uid inplace of name and name inplace of uid.
2.) However dictionaries are also unordered but in case of dictionaries only order of key-value pairs can be changed
    and the key or value itself will never be changed. 
    Hence we can unpack iterables containing dictionaries using this method.
3.) In python 3.6 or above, the key-value pair of a dictionary are iterated over in the same order in which
    they were inserted. So if you are using python 3.6 or above then even the order of key-value pairs will also 
    not change in iterator unpacking.
4.) We have already learned that a set can contain only a hashable object.
    So if the outer iterable is set, we can have only tuple as the inner iterable.
    As other iterables like lists and dictionaries are not hashable objects.
    So if you replace tuple with a list or a dictionary in example 3, then it will throw error - 
    TypeError: unhashable type: 'list' or unhashable type: 'dict'.Based on what you replaced tuple with.
"""