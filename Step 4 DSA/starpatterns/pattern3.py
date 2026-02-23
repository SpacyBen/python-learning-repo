def pyramid():
    n = 5
    print("pyramid")
    for i in range(n):
        for j in range(i,n-1):
            print(" ", end="")
        for k in range(i+1):
            print("*", end=" ")
        print()
def doublehill():
    n = 5
    print("double hill")
    for i in range(n):
        for j in range(i,n-1):
            print(" ", end="")
        for k in range(i+1):
            print("*", end=" ")
        for l in  range(i,n+1-i):
            print(" ", end="")
        for m in range(i+1):
            if m != n-1:
                print("*", end=" ")
        print()

def reverse_pyramid():
    n = 5
    print("reverse pyramid")
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(i,n):
            print("*", end=" ")
        print()

def butterfly():
    n = 4
    print("butterfly")
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        for k in range(i,n+1-i):
            print("-", end=" ")
        for j in range(i+1):
            if j != n-1:
                print("*", end=" ")
        print()
    for i in range(n-1):
        for j in range(i,n-1):
            print("*", end=" ")
        for k in range(i+1+i):
            print("-", end=" ")
        for m in range(i,n-1):
            print("*", end=" ")

        print()

def sandglass():
    n = 4
    print("sandglass")
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(i,n):
            print("*", end=" ")
        print()
    for i in range(1,n):
        for j in range(i,n-1):
            print(" ", end="")
        for k in range(i+1):
            print("*", end=" ")
        print()
        

print(pyramid())
print(doublehill())
print(reverse_pyramid())
print(butterfly())
print(sandglass())