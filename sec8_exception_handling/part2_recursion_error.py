"""
It is related to Stack and often occurs in case of recursive function i.e functions which call itself or two functions
which call each-other.
If recursive functions are not properly managed i.e if they don't stop calling functions repeatedly then after a
certain point it will throw RecursionError. Recursion errors are recoverable and hence can be handled. But it is
advised that manage you recursive functions properly so that function calling stops after reaching some conditions and
hence you don't need to handle RecursiveError.
"""
# Ex1 :-
def my_func(count):
    count += 1
    print("My function is called : ", str(count))
    return my_func(count)

my_func(0)


