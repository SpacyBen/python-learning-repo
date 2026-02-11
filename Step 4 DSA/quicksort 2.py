def partition(array,low,high):
    pivot = array[high]
    i = low - 1 #i =2 [3, 9, 7, 11, 12]  
    print(i,low,high,pivot)

    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[high] = array[high], array[i+1]
    print(array,i,low)
    
    return i + 1
    #i =2 low = 2 high = 2

def quicksort(array,low = 0, high = None):
    if high == None:
        high = len(array) - 1
    
    if low < high:
        pivot = partition(array,low, high)
        print("pivot",pivot)
        quicksort(array,low,pivot-1)
        quicksort(array,pivot+1,high) # 3 4
    

my_array = [11, 9, 12, 7, 3]
quicksort(my_array)
print("Sorted array:", my_array)