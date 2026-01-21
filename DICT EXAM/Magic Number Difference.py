list1 = [10, 3, 7, 2, 8]
list2 = [4, 6, 2, 10, 5]
difference = []
for a,b in zip(list1, list2):
    difference.append(abs(a-b))
print(f'Index {difference.index(max(difference))} has largest difference of {max(difference)}')