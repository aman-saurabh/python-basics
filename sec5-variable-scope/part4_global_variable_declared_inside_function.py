"""
In the previous part we have learned that any variable declared outside of any function is known as global variable.
And scope of such variables is global.
But we can declare a global variable directly inside a function also and scope of such variable will be global as well.
We can achieve that with the help of 'global' keyword
"""
# Ex :-
def global_variable_declaration_inside_function():
    global x
    # Here we are declaring global variable 'x' inside the function directly
    # i.e we haven't declared 'x' outside the function anywhere.
    x = 250
    print("Inside function value of x : ", str(x))

global_variable_declaration_inside_function()
print("Outside function value of x : ", str(x))
# But here please note that before accessing global variable 'x' outside the function,
# we must call the function in which the global variable is declared
# i.e 'global_variable_declaration_inside_function' function.
# Otherwise the global variable 'x' won't exist at the time you are trying to access it.
