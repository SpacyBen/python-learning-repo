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
    


def subcount2(arr,k):
    freq = {0:1}
    curr = 0
    count = 0
    for num in arr:
        curr += num
        if curr - k in freq:
            count += freq[curr - k]
        freq[curr] = freq.get(curr,0) + 1
    
    return count






if __name__ == "__main__":
    #array
    arr = [1, 2, 3, 2, 5]
    k = 5
    #all prefixsum in addition.
    prefsums = prefsum(arr)
    print(range1(prefsums,2,4))
    #queries can be used for user input ranges
    queries = [(0, 2), (1, 3), (2, 4), (3, 4)]
    for s,e in queries:
        print(range1(prefsums,s,e))
    print(prefsums)
    print(pref2(arr))
    print("=======")

    print(subcount2(arr,k))
