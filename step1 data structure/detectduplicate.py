def data1(a1):
    occure = []
    seen = set()
    duplicate = {}
    for w in a1:
        if w not in seen:
            occure.append(w)
            seen.add(w)
        if w in duplicate:
            duplicate[w] = duplicate.get(w) + 1
        else:
            duplicate[w] = duplicate.get(w,0) + 1
    for laman in list(duplicate.keys()):
        print(laman)
        if duplicate[laman] <= 1:
            del duplicate[laman]
    return duplicate, occure
def data2(a2):
    occure = {}
    for w in a2:
        if w in occure:
            occure[w] = occure.get(w) + 1
        else:
            occure[w] = occure.get(w,0) + 1
    return occure

word = ["banana","saging","banana","apple"]
dupe, occ = data1(word)
print(occ)
print("Duplicates: ",dupe)
print(data2(word))