def rev(s):
    if len(s) == 0:
        return s
    return rev(s[1:]) + s[0]

print(rev("Hello World"))
s = "Hello World"
print(s[:1])