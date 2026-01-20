def test(x, y):
    y = x + y
    x = y + x
    return x, y

a = 3
b = 5
x, y = test(a, b)
print("a =", a, "b =", b)
print("x =", x, "y =", y)