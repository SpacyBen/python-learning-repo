def data1(a1):
    occure = {}
    for char in a1:
        if char not in occure:
            occure[char] = 1
        else:
            occure[char] += 1
    return occure

word = "banana"
print(data1(word))