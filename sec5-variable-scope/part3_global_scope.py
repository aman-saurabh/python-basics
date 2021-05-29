"""
A variable declared in the main body of the Python file(or module) is called global variable and
belongs to global scope. Global variables are available anywhere within the file i.e inside any function
as well as outside any function, but we can't modify a global variable inside a function directly.
For such requirement we need to use 'global' keyword with the variable name in the function
from where we want to modify the value.
#Note :-
If you want to declare a global variable with 'global' keyword inside a function then do it before using it.
i.e even before accessing them, otherwise it will throw error as follows -
SyntaxError: name 'x' is used prior to global declaration.
i.e you can access a global variable even without using 'global' keyword inside a function.
But if you are using 'global' keyword for the same variable variable inside the same function, then do it
even before accessing them, otherwise it will throw error.
"""

x = 100
# Ex1 :- Accessing global variable without using 'global' keyword.
def global_scope_demo1():
    print("Accessing global variable x without using 'global' keyword : ", str(x))
global_scope_demo1()

# Ex2 :- Modifying global variable without using 'global' keyword.
def global_scope_demo2():
    # Modifying global variable 'x'
    # x += 100
    # Above line will throw error as we are trying to modify a global variable inside a function
    # For such requirement we need to use 'global' keyword with variable 'x'
    # However we can modify 'x', even without 'global' keyword as follows
    x = 200
    print("Inside function value of x : ", str(x))
    # It seems like we have modified global variable 'x' even without 'global' keyword.
    # But here actually we haven't modified the global variable.
    # Actually with above line od code we have created a new local variable 'x'
    # which has nothing to do with global variable 'x'.Hence if we print global variable 'x' outside this function.
    # We will get same value of it, as it was earlier(i.e 100) and not the modified value(i.e 200)

global_scope_demo2()
print("Outside function value of x : ", str(x))

# Ex3 :- Modifying global variable using 'global' keyword.
# But accessing the same global variable before declaring that variable with 'global' keyword
def global_scope_demo3():
    print("Accessing global variable x before using 'global' keyword : ", str(x))
    # global x
    # x += 100
    # print("Accessing global variable x after modification : ", str(x))

    # Above code will throw error, hence commented. As we are accessing global variable 'x' before
    # and then we are declaring that as 'global'

global_scope_demo3()


# Ex4 :- Modifying global variable using 'global' keyword.
# And accessing that global variable after declaring that variable with 'global' keyword
def global_scope_demo4():
    global x
    print("Accessing global variable x before modification : ", str(x))
    x += 100
    print("Accessing global variable x after modification : ", str(x))

global_scope_demo4()
print("Value of x now outside the function : ", str(x))
