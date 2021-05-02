import random
"""
In python 3.8 a new type of expression was introduced known as "Assignment expressions".
Assignment expression are written with a new notation (:=).This operator is known as the walrus operator.
Assignment expressions allow you to assign and return a value in the same expression.
For example, if you want to assign a value to a variable and print its value, then you typically do something like this:
my_var = 15
print(my_var)
As we can see we have to perform these operation in two lines.
But In Python 3.8, we can combine these two statements into one, using the walrus operator as follows:
print(my_walrus := 21)
It will print the value in the console as well as store the value in the specified variable 'my_walrus' for further use.
i.e if we print 'my_walrus' again it will print the same value.
So as we can see we can perform two types of operations in a single statement using walrus operator.
"""
# Example of Assignment expressions
# Example1 :-
my_nums = [1, 2, 3, 4, 5]
# Without walrus operator :
if len(my_nums) > 3:
    print(f'The length of the given list is {len(my_nums)}, which is greater than expected.')
# Here as we can see we have to use len() method twice.It would not be the case if we had used assignment expressions.
# With the help of walrus operator
if (n := len(my_nums)) > 3:
    print(f'The length of the given list is {n}, which is greater than expected.')

# Example2 :-
a = 5
b = 7
# Without using assignment expression
sum1 = a + b
if sum1 % 2 == 0:
    print("Sum is even")
elif sum1 % 5 == 0:
    print("Sum isn't even but multiple of 5")
else:
    print("Sum is neither even nor multiple of 5")

# With the help of assignment expression(i.e walrus operator)
x = 3
y = 8
if (sum2 := (x + y)) % 2 == 0:
    print("Sum is even")
elif sum2 % 5 == 0:
    print("Sum isn't even but multiple of 5")
else:
    print("Sum is neither even nor multiple of 5")

# Note :- Parenthesis has very important role in assignment expression(infact in any expression).
# So we need to take special care of parenthesis while using assignment expression.
# Otherwise we might get unexpected output.For instance, in the above example if we don't use parenthesis in the
# assignment expression or even if we use but in some other position then the output might be different.

# Walrus operator with list comprehension
def get_weather_data():
    return random.randrange(90, 110)

hot_temp = [temp for _ in range(20) if(temp := get_weather_data()) > 100]
print(hot_temp)
# Since here we don't need the item of range function, so we have used "_" for member.
# But if you want you can use any valid variable name also like 'i', 'm', 'num' etc.
