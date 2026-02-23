def dt():
    n = 5
    print("DT")
    for i in range(n):
        for j in range(i,n):
            print("*", end = "")
        print()
def rt():
    n = 5
    print("RT")
    for i in range(n):
        for j in range(i,n-1):
            print(" ", end = "")
        for k in range(i+1):
            print("*", end = "")
        print()
def lt():
    n = 5
    print("LT")
    for i in range(n):
        for j in range(i):
            print(" ", end = "")
        for k in range(i,n):
            print("*", end = "")
        print()

def hill():
    print("hill")
    n = 5
    for i in range(n):
        for j in range(i,n-1):
            print(" ", end="")
        for k in range(i+1):
            print("*", end="")
        for l in range(i+1):
            print("*", end="")
        print()
def reverse_hill():
    n = 5
    print("rev hill")
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(i,n):
            print("*", end="")
        for l in range(i,n):
            print("*", end="")
        print()
def hill2():
    n = 5
    print("hill2")
    for i in range(n):
        for j in range(i,n-1):
            print(" ", end="")
        for k in range(i+1):
            print("*", end="")
        for l in range(i):
            print("*", end="")
        print()
def reverse_hill2():
    n = 5
    print("reverse hill2")
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(i,n):
            print("*", end="")
        for l in range(i+1,n):
            print("*", end="")
        print()
def diamond():
    n = 5
    print("diamond")
    for i in range(n-1):
        for j in range(i,n-1):
            print(" ", end="")
        for k in range(i+1):
            print("*", end="")
        for l in range(i):
            print("*", end="")
        print()
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(i,n):
            print("*", end="")
        for l in range(i+1,n):
            print("*", end="")
        print()
            

ls = 4
rs = 7
n = 6
for i in range(1,n):
    if i == n-1:
        print(((ls-i)+1)*" " + "*" * (2*i-1) + ((rs)*"-") + "*" * (2*(i-1)))
    else:
        print(((ls-i)+1)*" " + "*" * (2*i-1) + ((rs)*"-") + "*" * (2*i-1))
    rs -= 2

print(dt())
print(rt())
print(lt())
print(hill())
print(reverse_hill())
print(hill2())
print(reverse_hill2())
print(diamond())