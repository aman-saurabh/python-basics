"""
If two or more variables with same name are declared in different scopes then which variable will get priority
(i.e which variable will be used if we try to access them) is defined by 'LEGB' rule.
LEGB rule :-
L -> Local
E -> Enclosing function(variable declared in outside function)
G -> Global
B -> Built-in modules i.e name preassigned in the built-in modules like open, int, str etc.
"""
# Ex :-
int = 100                   # --> line1

def outer_func():
    int = 200               # --> line2

    def inner_func():
        int = 300           # --> line3
        print(int)
    inner_func()

outer_func()
# Now output will  be 300, since local variable will get preference.
# But if we comment line 3, then output will be 200, i.e variable declared in outer function will get priority
# And if we comment line 2 also, then output will be 100, i.e global variable value will be used
# And if we comment line 1 also, then output will be <class 'int'> i.e built-in module's value will be considered.
