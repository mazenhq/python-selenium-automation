# When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15


# code here
n = 7  # 29

saved_n = n
result = 1

while n > 0:
    result = result + n
    n = n - 1

print(f'The factorial of {saved_n} = {result}')