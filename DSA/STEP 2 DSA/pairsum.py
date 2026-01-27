def pair1(arr,target):
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target:
            print(f"{arr[l]} + {arr[r]} = {target}")
            l += 1
            r -= 1

def pair2(arr, target):
    for i in range(len(arr)):
        print(i)
        adds = []
        adds.append(arr[i])
        while sum(adds) != target:
            for j in range(len(arr)):
                if arr[j] in adds:
                    continue
                if sum(adds) == target:
                    print(adds)
                    print("----")
                    adds = []
                    break
                else:
                    adds.append(arr[j])
                    print(adds)
    
                



        
        



arr = [1,2,3,4,5,6,7,8,9]
target = 10
pair1(arr,target)
pair2(arr,target)