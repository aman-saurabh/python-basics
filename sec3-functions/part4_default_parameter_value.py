"""
While defining a function we can set default value for any parameter.
This value is known as default parameter value
and it will be used in case while calling the function user don't pass any argument for that parameter.
Note :-
Parameters with default value must be placed at the end within the parenthesis of any function
i.e after all parameters that has no default value.
"""
# Example :-
def my_function(name, country="India"):
    print(f"Hi, I am {name} and I am from {country}")

# With country argument - Given value will be used for country parameter
my_function("Mike", "USA")
# Without country argument - Default value will be used for country parameter
my_function("Aman")