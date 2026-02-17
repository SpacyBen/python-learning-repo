def bensort(arr):
    n = len(arr)
    low = 1
    prevlow = 1
    i = low - 1
    while i < n:
        print(low)
        print(arr)
        if arr[low] < arr[i]:
            arr[low], arr[i] = arr[i], arr[low]
        low += 1
        if low == n:
            prevlow += 1
            if prevlow == n:
                break
            low = prevlow
            i += 1
    return arr



arr = [5,2,6,7,1] 
print(bensort(arr))

#[5,2,6,7,1]
#[2,5,6,7,1]
#[1,5,6,7,2]
