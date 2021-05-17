# Example of how to use recursive function to sum of first n numbers.
def number_limit_sum(num, accumulator=0):
    return accumulator if num == 0 else number_limit_sum(num-1, accumulator+num)

n = 10
s = number_limit_sum(10)
print(f"Sum of first {n} numbers is : {s}")
