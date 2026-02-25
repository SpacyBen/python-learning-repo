def count(n):
    if n == 0:
        return 0
    return 1 + count(n // 10)

def count2(n):
    if n == 0:
        return 0
    return count2(n[1:]) + 1
print(count(25))
print(count2(25))
n = 123451
print(n // 10)