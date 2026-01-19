arr1 = [4, 7, 2, 9, 5]
arr2 = [3, 8, 5, 6, 10]
maxarr = []

def compare_arrays(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            maxarr.append(arr1[i])
        else:
            maxarr.append(arr2[i])

compare_arrays(arr1, arr2)
print(maxarr)