tup = ({200: "Aman"}, {120: "Monty"}, {150: "Vineet"})

for pair in tup:
    # Since dictionary can have multiple key-value pairs.Hence we have to run another loop for each key-value pair.
    for uid, name in pair.items():
        print(f"Uid : {uid}, Name : {name}")
else:
    print("Unpacking of tuple of dictionaries using for loop completed")

"""
Notes :-
1.) In outer loop lists, sets and tuples are allowed.
    But if you use set as outer loop then only tuple is allowed in inner iterable. 
    Dictionaries can also be used in outer loop but in that case unpacking will be different 
    as their structure and functionality is different.
2.) In inner loop lists, tuples and dictionaries are allowed. Here also dictionaries will works differently.
3.) If dictionary is used in iterator unpacking either as outer iterable or as inner iterable, 
    we have to unpack it differently, as structure and functionality of dictionaries are different.
    For example we can see in previous example that unpacking of dictionary in inner loop is different than others.
4.) If using set or dictionary in outer loop then you can use only for loop. As they supports only normal 'for' loop.
"""