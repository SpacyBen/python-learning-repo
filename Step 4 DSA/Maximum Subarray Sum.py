def maxsimum1(arr,k):
    n = len(arr)
    output = [0] * n
    l,r = 0,1
    currentsum = 0
    maxsum = 0
    valmax = []
    while l < n:
        output[l] = arr[l]
        output[r] = output[r-1] + arr[r]
        if output[r] > maxsum and output[r] <= k:
            maxsum = output[r]
        r += 1
        if r == 5:
            print(output)
            output = [0] * n
            l += 1
            r = l + 1
        if r > n-1:
            output[l] = arr[l]
            break
        
    return output,maxsum

    



if __name__ == "__main__":
    arr = [2, 1, -3, 4, 5]
    k = 6
    print(maxsimum1(arr,k))
