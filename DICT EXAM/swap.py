def odd(num):
    return num % 2 != 0

a = int(input("a = "))
b = int(input("b = "))

if odd(a + b):
    temp = a
    a = b
    b = temp
    print("After swapping: a =", a, "b =", b)
else:
    a = a * 2
    b = b * 2
    print("After Even: a =", a, "b =", b)
