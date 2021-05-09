# Like lists, we can run 3 types of loops on a tuple :-
my_tuple = ("Aman", "Mohan", "Pawan", "Vinay", "Aman", "Pankaj", "Sapna", "Samir")

# for loop :-
for item in my_tuple:
    print(item)

# 2.) for loop with range() and len() functions :-
for item in range(len(my_tuple)):
    print(my_tuple[item])

# 3.) while loop :-
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i = i + 1

# break, continue and pass statements in loop
# Rules for break, continue and pass statements for tuples also are same as in case of lists
