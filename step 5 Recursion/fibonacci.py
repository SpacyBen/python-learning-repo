def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    print(f"Calculating fib({n})")
    return fib(n - 1) + fib(n - 2)
print(fib(5))