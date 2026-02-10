def oN1(arr,n):
    output = [1] * n
    #[1,1,1,1,1]
    #[1,1,2,1,1]
    #[1,1,2,6,24]
    #[1,1,2,6,24]

    #left
    for i in range(1,n):
        output[i] = output[i-1] * arr[i-1]

    #right
    right = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * right
        right *= arr[i]
    #i = 4
    #[1,1,2,6,24]
    #i=3 and right = 5
    #[1,1,2,30,24]
    #i=2 and right = 20
    #[1,1,40,30,24] and so on
    return output

arr = [1,2,3,4,5]
n = len(arr)
print(oN1(arr,n))
