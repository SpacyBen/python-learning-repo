def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n == 0:
        return
    factorial(n - 1)
    print(n, end = " ")
    return n * factorial(n - 1)

print(factorial(3))