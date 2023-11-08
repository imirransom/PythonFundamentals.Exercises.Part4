def factorial_recursion(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n -1)

num = int(input())

print(factorial_recursion(num))