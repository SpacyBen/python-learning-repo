#mostcommonelement
def data1(a1):
    occure = {}
    for w in a1:
        if w in occure:
            occure[w] = occure.get(w) + 1
        else:
            occure[w] = occure.get(w,0) + 1
    maxs = max(occure, key = occure.get)

    return maxs,occure[maxs]


word = "banana"
com,val = data1(word)
print(f"Most Common Element: \"{com}\" with {val}")
