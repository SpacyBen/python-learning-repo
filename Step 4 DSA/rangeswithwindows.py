
def prefix(arr,t):
    arr2 = []
    curr = 0
    output = []
    count = 0
    for i in arr:
        curr += i
        arr2.append(curr)
    print(arr2)
    l,r = 0,1
    prev = l
    while r < len(arr):
        prev = l
        
        print("----arr")
        print(arr[prev],arr[r])
        print("----arr")

        if (arr2[r] - arr2[l-1]) == t:
            if arr[r] == arr[prev]:
                output.append(arr[r])
                print("yes")
            else:
                output.append(arr[l])
                output.append(arr[r])
                print("ben")
        
        r += 1
        l += 1
        print("----")
        print(l,r,prev)
    
    return output






arr = [1,2,3,2,5]
t = 5
print(prefix(arr,t))
