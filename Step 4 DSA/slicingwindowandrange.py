def subarrays_with_sum(arr, target):
    count = 0
    result = []
    n = len(arr)

    # build prefix sum
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    # check all subarrays (O(n^2) approach)
    for start in range(n):
        for end in range(start, n):
            if prefix[end + 1] - prefix[start] == target:
                count += 1
                result.append(arr[start:end + 1])

    return count, result

# Example
arr = [1, 2, 3, 2, 5]
target = 5
count, subarrays = subarrays_with_sum(arr, target)
print("Count:", count)
print("Subarrays:", subarrays)
