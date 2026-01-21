arr1 = [4, 7, 2, 9, 5]
arr2 = [3, 6, 8, 4, 5]
output = []
for a,b in zip(arr1, arr2):
    if a > b:
        output.append(a-b)
output.sort(reverse=True)
sum = sum(output)
print("Differences in descending order:", output)
print("Sum of differences:", sum)