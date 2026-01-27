
def rev1(arr):
    return arr[::-1]

def rev2(arr):
    arr2 = arr.copy()
    l,r = 0, len(arr2) - 1
    while l < r:
        arr2[l],arr2[r] = arr2[r],arr2[l]
        l += 1
        r -= 1
    return arr2

def rev3(arr):
    arr2 = []
    i = len(arr) - 1
    while i >= 0:
        arr2.append(arr[i])
        i -= 1
    return arr2

arr = [1,2,3,4,5]
print(rev1(arr))
print(rev2(arr))
print(rev3(arr))
