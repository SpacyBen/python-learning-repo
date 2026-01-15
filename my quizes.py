#Input two lists of 5 numbers each.
#Find which index has the largest difference (absolute value).
#Print both the index and the difference.

list1 = [10, 3, 7, 2, 8]
list2 = [4, 6, 2, 10, 5]
list3 =[]
diff = list1[0] - list2[0]
name = "Index 0"
for i in range(len(list1)):
    if list1[i] < list2[i]:
        result = int(((list1[i] - list2[i])*-2)/2)
        list3.append(result)
    else:
        result = (list1[i] - list2[i])
        list3.append(result)
print(list3)
print(f"Index {list3.index(max(list3))} has the largest difference: {max(list3)}")



