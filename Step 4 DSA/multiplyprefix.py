def pref1(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n
    output = []
    for i in range(len(arr)):
        if i == 0:
            left[0] = arr[i]
        else:
            left[i] = left[i-1] * arr[i-1]
   
    for i in range(len(arr)-1,-1,-1):
        print(i)
        if i == (len(arr)-1):
            right[i] = arr[i]
        elif i == (len(arr)-2):
            right[i] = arr[i+1]
        else:
            right[i] = right[i+1] * arr[i+1]
    
    for i in range(len(arr)):
        output.append(left[i] * right[i])
    return left,right,output



arr = [1,2,3,4,5]
print(pref1(arr))

