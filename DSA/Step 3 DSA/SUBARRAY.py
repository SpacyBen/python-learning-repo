def sub1(arr):
    arr2 = []
    l,m,r = 0,1,2
    while r < len(arr):
        arr2.append(arr[l])
        arr2.append(arr[m])
        arr2.append(arr[r])
        print(arr2)
        l += 1
        m += 1
        r += 1
        arr2 = []

def sub2(arr):
    l,r = 0,3
    while r < len(arr):
        print(arr[l:r])
        l += 1
        r += 1

def sub3(arr,l,s):
    for r in range(l,len(arr) + 1):
        print(arr[s:r])
        s += 1
        

        

arr = [1,2,3,4,5,6,7,8,9]
sub1(arr)
print("------------")
sub2(arr)
print("------------")
sub3(arr,5,1)

