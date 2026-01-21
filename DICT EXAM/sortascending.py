nums = [12, 5, 8, 20, 3, 17]
sorted_nums = sorted(nums)
average = sum(sorted_nums)/len(sorted_nums)
output = []
print(average)
for i in sorted_nums:
    if i > average:
        output.append(i)
print("Original list:", nums)
print("Sorted list in ascending order:", sorted_nums)
print("Numbers greater than average:", output)