#  *  
# ***
#*****

n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()


for i in range(1,n):
    print("*" * i + " " * (n-i) +" " * (n-i-1) + "*" * (i))
    if i == n-1:
        print("*" * n + "*" * (n-1))
for k in range(n-1,0,-1):
    print("*" * k + " " * (n-k) +" " * (n-k-1) + "*" * (k))
print("----")
n = 5
width = 2*n - 1

for i in range(1, n+1):
    gap = width - 2*i
    if gap < 0:
        gap = 0
    print("*"*i + " "*gap + "*"*i if gap else "*"*width)

for i in range(n-1, 0, -1):
    gap = width - 2*i
    print("*"*i + " "*gap + "*"*i)
