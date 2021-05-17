# Example of how to use recursive function to get factorial of a number.
def get_factorial(n):
    if n == 1:
        return 1
    else:
        return n * get_factorial(n - 1)

num = 5
factorial = get_factorial(num)
print(f"Factorial of {num} is : {factorial}")
