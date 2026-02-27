def total(n):
    if n == 0:
        return 0
    print(n)
    return (n%10) + total(n//10)


#i know the problem here this is my first try i save it to notice the difference. the problem here is if left > right it doesnt check
def isSorted(arr,left,right):
    print(arr)
    if len(arr) == 2:
        return arr[left] < arr[right]
    if arr[left] < arr[right]:
        return isSorted(arr[1:],left,right)


#idk if theres more best way but its good recursion for me the print just for debug
def isSorted2(arr,left,right):
    print(arr)
    if len(arr) == 2:
        return arr[left] < arr[right]
    return arr[left] < arr[right] and isSorted2(arr[1:],left,right)

#ill finish this tomorrow or soon.
# def isSorted3(arr,index = 0):
#     print(arr)
#     if len(arr) == 2:
#         return arr[left] < arr[right]
#     return arr[left] < arr[right] and isSorted2(arr[1:],left,right)
        
    
    
    
print(total(12345))
print("------")
arr = [1, 2, 4, 5, 5, 6]
left = 0
right = 1
print(isSorted(arr,left,right))
print(isSorted2(arr,left,right))
