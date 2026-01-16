mydict = {
    1 : "ben",
    3 : "ben",
    7 : "jerry",
    2: "sally",
    9 : "tom",
    6 : "tom"
}
sorted_dict = dict(sorted(mydict.items()))
word_sort = {}
for f,w in sorted_dict.items():
    if w in word_sort:
        word_sort[w] += 1
    else:
        word_sort[w] = 1
    print(word_sort)
