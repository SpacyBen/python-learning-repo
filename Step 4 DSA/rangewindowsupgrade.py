
def prefix(arr,t):
    arr2 = []
    curr = 0
    seen = set()
    output = []
    for i in arr:
        curr += i
        arr2.append(curr)
    print(arr2)
    l,r = 0,1
    while r < len(arr2):
        if l == 0:
            if (arr2[r]) == t:
                seen.add(l)
                seen.add(r)
        elif (arr2[r]-arr2[l-1]) == t:
            seen.add(l)
            seen.add(r)
        l += 1
        r += 1
    count = len(seen)
    print(len(seen))
    for i in seen:
        output.append(arr[i])
    print(output,count,seen)


arr = [1,2,3,2,5]
t = 5
prefix(arr,t)
