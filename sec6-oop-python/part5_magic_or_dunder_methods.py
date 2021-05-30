"""
Magic methods or dunder methods in python are special methods which are not meant to be invoked directly by
the programmer, But the invocation happens internally by the class on a certain action.For example :-
When you add two numbers using "+" operator internally the "__add__()" method is called.Similarly when you call len()
method for string, list, tuple, set etc. internally "__len__()" method is called and when you call "str()" function for
any object internally it calls "__str__()" method.These methods are known as magic methods or dunder methods.
There are several magic methods or dunder methods available in python.Every build-in class in Python defines
many of these methods to provide functionalities for several operations.Like '__add__()' for "+" operator,
'__sub__()' for "-" operator, '__or__()' for "or" operator etc.Apart fro that it is also defined to provide
functionalities for several common methods as well like '__str__()' for "str()" method, '__int__()' for "int()" method
and '__len__()' for "len()" method etc.
We can check the list of all methods(i.e magic methods + general methods) of a class using "def()" method.
For example we can check list of all methods of 'int' class by calling "def(int)" method.
We can define dunder or magic methods in our custom class also to provide functionality for
such common operators and methods.
Note :- Dunder is created from two words "Double" and "Under"(short form for "Underscores").
It is named so because every dunder or magic methods have two prefix and two suffix underscores in the method name.
"""
# Example :- Defining and using magic methods in our custom class :
class Home:
    def __init__(self, owner, year, area):
        self.owner = owner
        self.year = year
        self.area = area

    def __str__(self):
        # Its return type is string.Hence we must return a String value.
        return f"This is {self.owner}'s house built in year {self.year}, on area of {self.area}"

    def __len__(self):
        # Its return type is int.Hence we must return a int value.
        return self.area

my_home = Home("Aman", 2015, 5000)
print(str(my_home))
print(len(my_home))


