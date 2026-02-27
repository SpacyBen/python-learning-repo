def climb(n):
    print("n: ", n)
    if n <= 1:
        return 1
    return climb(n-1) + climb(n-2)

print(climb(3))