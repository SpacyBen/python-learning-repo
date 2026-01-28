def pair1(arr,target):
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target:
            print(f"{arr[l]} + {arr[r]} = {target}")
            l += 1
            r -= 1

def pair2(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for f in range(j + 1, n):
                if arr[i] + arr[j] + arr[f] == target:
                    print(f"{arr[i]} + {arr[j]} + {arr[f]} = {target}")

def pair3(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for f in range(j + 1,n):
                for g in range(f + 1, n):
                    if arr[i] + arr[j] +arr[f] +arr[g] == target:
                        print(f"{arr[i]} + {arr[j]} + {arr[f]} + {arr[g]} = {target}")


arr = [1,2,3,4,5,6,7,8,9]
target = 10
pair1(arr,target)
pair2(arr,target)
pair3(arr,target)