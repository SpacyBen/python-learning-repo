def pref1(arr):
    n = len(arr)
    left = [1] * n
    right = [1] * n
    output = []
    for i in range(1,n):
        left[i] = left[i-1] * arr[i-1]
   
    for i in range(len(arr)-2,-1,-1):
        print(i)
        right[i] = right[i+1] * arr[i+1]
    
    for i in range(n):
        output.append(left[i] * right[i])
    return left,right,output



arr = [1,2,3,4,5]
print(pref1(arr))

