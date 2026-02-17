def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):  # last i elements are already sorted
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break  # array is already sorted
        print(arr)
    return arr

arr = [5, 2, 6, 7, 1]
print("Sorted array:", bubble_sort(arr))
