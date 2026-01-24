def data1(a1):
    occure = []
    seen = set()
    duplicate = {}
    for w in a1:
        if w not in seen:
            occure.append(w)
            seen.add(w)
        elif w in duplicate:
            duplicate[w] = duplicate.get(w) + 1
        else:
            duplicate[w] = duplicate.get(w,0) + 1
    return duplicate, occure


word = ["banana","saging","banana","apple"]
dupe, occ = data1(word)
print(occ)
print("Duplicates: ",dupe)