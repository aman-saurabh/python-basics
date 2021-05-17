"""
If you don't know how many arguments will be passed into  a function,
then use single variable for all unknown arguments and
place that variable as the last argument and add (*) before that variable.
Such arguments are called arbitrary argument.
"""
# Example :-
def my_function(user, *friends):
    print("User name is : ", user)
    print("User's relatives are as follows : ")
    for i in range(len(friends)):
        print(f"{str(i+1)} - {friends[i]}")
# Here we could have used normal for loop also but using this syntax make it more clear
# that how to use arbitrary arguments.
my_function("Aman", "Rohan", "Mohit", "Priyanka")
