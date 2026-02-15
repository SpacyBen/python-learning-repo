def reverse_array(arr):
    n = len(arr)
    left,right = 0, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))