"""
In this part we will see how to get and set recursion limit with an example.
"""
import sys

print("Default recursion limit : ", sys.getrecursionlimit())

# Setting new value for recursion limit
sys.setrecursionlimit(10 ** 6)

print("Current recursion limit : ", sys.getrecursionlimit())


def my_func(count):
    try:
        count += 1
        print("My function called.Count is : ", str(count))
        return my_func(count)
    except RecursionError:
        print("Maximum recursion limit is reached at count : ", str(count))
    except:
        print("Some other error occurred")

my_func(0)

"""
Here we can see after reaching approximately 20900-20950 count only it was stopped and even it didn't throw any error,
neither RecursionError nor any other error.It is because after so much recursions the execution was interrupted 
by python compiler and hence it stopped abruptly.If you run this program multiple times you will see maximum count is 
different in different attempts(however will be nearby 20900-20950 only).So it is not recommended to set recursion limit
a very large value.Infact in this example the function is very simple and short so the recursion count goes up to 20950 
count.In real programs if the function is lengthy and complex then in such scenarios maximum recursion count can be 
less also.So it is not recommended to set recursion limit with a very large value.
In the above program if wqe had set new recursion limit as 20000 then the answer would be :
1000  
20000
my function called.Count is : 1
........
........
my function called.Count is : 19996
Maximum recursion limit is reached at count : 19997
"""