array1 = [3, 8, 5, 2, 8]
array2 = [4, 7, 6, 1, 10]
output = []
for a,b in zip(array1, array2):
    if a < b:
        output.append(b-a)
print(output)