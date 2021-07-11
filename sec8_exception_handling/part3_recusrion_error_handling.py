"""
In this part we will see how to handle RecursionError :-
Note :- We will learn about exception handling in Python in details later, here just see the syntax
and understand the logic.
"""

def my_func(count):
    try:
        count += 1
        print("My function called.Count is :"+str(count))
        return my_func(count)
    except RecursionError:
        print("Maximum recursion limit is reached at count : ", str(count))

my_func(0)
"""
If you run this program several times you will see every time maximum recursion limit is 997, 998 etc. 
It is because default recursion limit in python is 1000. And in these 1000 recursion calls 2-4 recursion
calls are wasted in internal function calls. So we get maximum recursion limit is 997, 998 etc.
We can reset it to another value based on our requirement using 'sys' module's "setrecursionlimit(newlimit)" method.
However you can pass any value in it as argument to set new limit but don't set it to a very large value (greater than
20000-21000), otherwise your function won't complete that much recursion and will be interrupted in the midway.
You can also check the current recursion limit using 'sys' module's "getrecursionlimit()" method.
We will see how to get and set recursion limit with an example in the next part.
"""