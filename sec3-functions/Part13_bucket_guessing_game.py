"""
Suppose there are 5 buckets and 4 of them are empty and in 1 bucket there is a ball.
User will guess the bucket number in which ball is there.
If he guess correct, we will display "Yeah! Correct answer.You won!"
And If he guess wrong, we will display "Wrong answer.Correct answer is {correct_bucket}.Please try again"
And will give him another chance.In total we will give him 3 chances and in 3 chances also
if he guess wrong we will print "Again wrong answer, you lost."

#Notes :-
1.) In this example we will use 'shuffle' method of 'random' module. Which is used to shuffle items of an iterable.
    We will learn about modules and packages in details later.Here just see how to use them.
2.) In this example we have also used 'global' keyword. Actually we can't modify a global variable
    (i.e variable defined outside of any function) directly inside a function, otherwise it will throw error
    however we can access them directly inside a function. If we need to modify a global variable inside any function,
    we need to use 'global' keyword for that variable inside the function. For example : 'global my_var'.
    Infact with the help of 'global keyword we can directly define a global variable from inside of a function also.
    We will learn about 'global' keyword in details while learning 'Variable scopes'.
"""
from random import shuffle

bucket_list = ['', 'ball', '', '', '']
count = 0


def shuffle_bucket_list(b_list):
    shuffle(b_list)
    return b_list


def guess_bucket():
    guess = input("Enter the bucket number in range of 1-5 : ")
    if guess in ['1', '2', '3', '4', '5']:
        check_guess(int(guess))
    else:
        print("Sorry.Your answer must be a number in range 1-5.Please try again")
        guess_bucket()


def check_guess(guess):
    global count
    count += 1
    shuffled_bucket = shuffle_bucket_list(bucket_list)
    bucket_number = shuffled_bucket.index('ball') + 1
    if guess == bucket_number:
        print("Yeah! Correct answer.You won.")
    else:
        if count < 3:
            print(f"Wrong answer.Correct answer is {bucket_number}.Please try again.")
            guess_bucket()
        else:
            print("Again wrong answer.You lost.")

guess_bucket()

