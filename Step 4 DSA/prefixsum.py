def prefsum(arr):
    if not arr:
        return []
    n = len(arr)
    prefixsum = [0] * n
    prefixsum[0] = arr[0]

    for i in range(1,n):
        prefixsum[i] = prefixsum[i - 1] + arr[i]
    return prefixsum

def pref2(arr):
    if not arr:
        return []
    n = len(arr)
    prefsum = []
    prefsum.append(arr[0])
    for i in range(1,n):
        formula = prefsum[i-1] + arr[i]
        prefsum.append(formula)
    return prefsum
def range1(prefsums,s,e):
    if s != 0:
        return prefsums[e] - prefsums[s-1]
    else:
        return prefsums[e]




if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    prefsums = prefsum(arr)
    print(range1(prefsums,2,4))
    queries = [(0, 2), (1, 3), (2, 4), (3, 4)]
    for s,e in queries:
        print(range1(prefsums,s,e))
    print(prefsums)
    print(pref2(arr))
