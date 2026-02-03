def count_subarrays(arr, k):
    freq = {0: 1}
    curr = 0
    count = 0

    for num in arr:
        curr += num
        if curr - k in freq:
            count += freq[curr - k]
        freq[curr] = freq.get(curr, 0) + 1

    return count,freq,curr

print(count_subarrays([1, 2, 3, 4, 5], 5))
