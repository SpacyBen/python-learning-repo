def max_subarray_sum_positive(arr, k):
    n = len(arr)
    max_sum = 0
    curr_sum = 0
    left = 0

    for right in range(n):
        curr_sum += arr[right]  # add new element to window

        # shrink window from left until sum ≤ k
        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        # update max sum
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum

# Example (all positive numbers)
arr = [2, 1, 4, 1, 5]
k = 6
print(max_subarray_sum_positive(arr, k))  # Output: 6
