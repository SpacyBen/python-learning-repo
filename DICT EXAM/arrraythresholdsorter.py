values = [12, 3, 8, 14, 7, 5]
threshold = 7
lessEqual = []
greater = []
for i in values:
    if i <= threshold:
        lessEqual.append(i)
    else:
        greater.append(i)
lessEqual.sort()
greater.sort()
print(lessEqual)
print(greater)