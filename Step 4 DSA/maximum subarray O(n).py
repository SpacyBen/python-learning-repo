def maxsub1(arr,k):
    n = len(arr)
    curr = 0
    maxsum = 0
    left = 0

    for right in range(n):
        curr += arr[right]

        while curr > k:
            curr -= arr[left]
            left += 1
        
        if curr > maxsum:
            maxsum = curr
    return maxsum

# Example (all positive numbers)
arr = [2, 1, 4, 1, 5]
k = 6
print(maxsub1(arr, k))  # Output: 6
