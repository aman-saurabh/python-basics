"""
Some times we see that even if there is no syntax error or indentation error in the program and nor there is any
recursion error or out of memory errors, but still program throws error and stops execution abruptly.
Generally such problems occurs due to some mistake in the logic of the programs and hence they are also known as
"Logical errors or Exceptions".
Types of Exceptions :
Exception1 :- TypeError
Raised when an operator or function is applied to an object of an inappropriate type.
"""
a = 10
b = input("Enter your desired number : ")           # line1
print(a+b)

# O/P :-
# if we enter -> 20
# output -> TypeError
"""
It will throw TypeError even if you entered "20" as desired number when asked.
It is because input function always return a "string" type value.So even though you entered number 20 when asked
but value of "b" will be string 20.So when we perform a+b, it tries to add a number(a) with a string(b) and hence
it throws "TypeError".We can solve it by replacing "line1" by following code :
b = int(input("Enter your desired number : "))
"""
