def data1(a1):
    occure = {}
    for char in a1:
        if char not in occure:
            occure[char] = 1
        else:
            occure[char] += 1
    return occure

def data2(a1):
    occure = {}
    for w in a1:
        if w in occure:
            occure[w] = occure.get(w) + 1
        else:
            occure[w] = occure.get(w,0) + 1
    return occure


word = "banana"
print(data1(word))
print(data2(word))