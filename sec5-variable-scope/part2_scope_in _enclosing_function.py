"""
In case of enclosing functions(i.e functions within the function) :-
If a function is defined inside another function, then any variable declared directly inside the outer function
is available inside the inner function also.
But its reverse is not true i.e in case of enclosing functions, a variable declared inside the inner function
is not available directly inside the outer function as it is outside the scope of that variable.
"""
# Ex1 :- Variable declared inside the outer function
def outer_function_variable():
    x = 100

    def inner_function():
        print("Calling x from inner function", str(x))

    inner_function()
    print("Calling x from outer function", str(x))

outer_function_variable()

# Ex2 :- Variable declared inside the outer function
def outer_function():

    def inner_function_variable():
        y = 200
        print("Calling y from inner function", str(y))

    inner_function_variable()
    # print("Calling x from outer function", str(y))
    # Above line will throw error,hence commented. As 'y' is outside the scope of outer function.
outer_function()
