def win1(arr,l,s):
    for r in range(l,len(arr) + 1):
        print(arr[s:r])
        print(f"Max: {max(arr[s:r])} and Min: {min(arr[s:r])}")
        s += 1

def win2(arr,l,s):
    arr2 = []
    for r in range(l,len(arr) + 1):
        arr2.append(arr[s:r])
        print(arr2)
        s += 1
    for i in arr2:
        print(f"Max: {max(i)} and Min: {min(i)}")

def win3(arr,l,s):
    for r in range(l,len(arr) + 1):
        print(arr[s:r])
        print(f"Max: {max1(arr[s:r])} and Min: {min1(arr[s:r])}")
        s += 1


def max1(arr):
    high = arr[0]
    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]
    return high

def min1(arr):
    low = arr[0]
    for i in range(len(arr)):
        if arr[i] < low:
            low = arr[i]
    return low
        

arr = [1,2,3,4,5,6,7,8,9]

print("------------")
win1(arr,5,1)
print("------------")
win2(arr,5,1)
print("------------")
win3(arr,5,1)