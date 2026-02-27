def power(n,e):
    print(n,e)
    if e == 0:
        return 1
    return n * power(n,e-1)
    
def occ(arr,t):
    print(arr,t)
    if len(arr) == 0:
        return 0
    if arr[0] == t:
        return 1 + occ(arr[1:],t)
    return occ(arr[1:],t)

#my first try the occ(arr,t) is my renewed version on occ2 i dont print it i just want to save it
def occ2(arr,t):
    print(arr,t)
    if len(arr) == 0:
        return 0
    if arr[0] == t:
        return 1 + occ(arr[1:],t)
    else:
        return 0 + occ(arr[1:],t)

def binary(arr,t,start,end):
    middle = (start + end)//2
    if start > end:
        return 'not found'
    if arr[middle] == t:
        return middle
    elif arr[middle] > t:
        return binary(arr,t,start,middle-1)
    elif arr[middle] < t:
        return binary(arr,t,middle+1,end)

    
print(power(5,3))
print("------------")
arr = [1, 2, 3, 2, 2, 4]
target = 0
print(occ(arr,target))
print("------------")
array = [1, 3, 5, 7, 9, 11, 13]
t = 9
start = 0
end = len(arr)-1
print(f"index {binary(array,t,start,end)}")

