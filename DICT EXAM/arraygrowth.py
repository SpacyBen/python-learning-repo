before = [2, 5, 7, 3, 9]
after  = [3, 6, 9, 2, 11]
for i in range(len(before)):
    if after[i] > before[i]:
        print(f"Index {i}: +{after[i] - before[i]}")