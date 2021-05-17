"""
If you don't know how many keyword arguments will be passed into a function,
then use single variable for all unknown arguments and
place that variable as the last argument and add (**) before that variable.
Such arguments are called arbitrary keyword argument.
i.e arbitrary keyword argument is exactly same as arbitrary argument,
the only difference is arbitrary keyword argument is used for keyword arguments
while arbitrary argument is used for normal arguments
"""
# Example :-
def my_function(name, **other_info):
    print("User's name is : ", name)
    print("User's other info are as follows : ")
    for info in other_info:
        print(info+" - "+str(other_info[info]))

my_function(name="Aman", age=30, location="Noida", designation="CEO")
