employees = ["Aman", "Mohan", "Pawan", "Parthiv", "Vinay"]
# 1.) for loop :-
for emp in employees:
    print(emp)

# 2.) for loop with range() and len() methods :-
for emp in range(len(employees)):
    print(employees[emp])

# 3.) while loop :-
i = 0
while i < len(employees):
    print(employees[i])
    i = i + 1

# break, continue and pass statements in loop
# 1.) break :-
# The break statement is used to exit out of a loop when an external condition is triggered.
# Generally the break statement is used within a loop, usually after a conditional if statement.
# Ex : The following loop will print numbers multiple of 7, but exit the loop when any number divisible by 10 is found.
for n in range(7, 100, 7):
    if n % 10 == 0:
        break
    print(f'Number is : {n}')
print("Loop demonstrating continue ends here.")

# 2.) continue :-
# The continue statement is used to skip the current iteration of the loop when an external condition is triggered.
# Like break statements they are also used within a loop, usually after a conditional if statement.
# Ex :- Same as previous one but this time we will not exit the loop when any number divisible by 10 is found.
# instead we will skip that number only and will continue with next numbers
for n in range(7, 100, 7):
    if n % 10 == 0:
        continue
    print(f'Number is : {n}')
print("Loop demonstrating continue ends here.")

# 3.) pass :-
# The pass statement doesn't have any significant meaning in the loop i.e
# After using the pass statement in this program also,
# the program will run exactly same as if there was no conditional statement in the program.
# Ex :- In previous examples, if we use pass inplace of 'break' or 'continue',
# we will see it doesn't make any impact on the program and program will flow as if there was no conditional statement.
for n in range(7, 100, 7):
    if n % 10 == 0:
        pass
    print(f'Number is : {n}')
print("Loop demonstrating pass ends here.")
# We could have achieved same result if we haven't applied 'pass' statement(infact complete 'if' statement in this case)
