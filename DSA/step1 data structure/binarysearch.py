def bin(sort1,target):
    if not sort1:
        return print("empty")
    first = 0
    last = len(sort1)-1
    mid = int(first + last//2)
    print(f"First: Index:{first} - {sort1[first]} , Mid: Index:{mid} - {sort1[mid]} , Last: Index:{last} - {sort1[last]} ")
    while True:
        if target < sort1[mid]:
            last = mid - 1
            mid = int((first + last)//2)
            print(f"First: Index:{first} - {sort1[first]} , Mid: Index:{mid} - {sort1[mid]} , Last: Index:{last} - {sort1[last]} ")
        elif target > sort1[mid]:
            first = mid + 1
            mid = int((first + last)//2)
            print(f"First: Index:{first} - {sort1[first]} , Mid: Index:{mid} - {sort1[mid]} , Last: Index:{last} - {sort1[last]} ")
        elif target == sort1[mid]:
            print(f"Found the target: {sort1[mid]} at Index: {mid}")
            break
    

arr = [3, 5, 6, 8, 10,11]
target =  8
sort = sorted(arr)
bin(sort,target)





    
