def subarrays_with_sum(arr, target):
    count = 0
    result = []
    n = len(arr)

    # build prefix sum
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i] #[0][1][3][6][8][13]

    # check all subarrays (O(n^2) approach)
    for start in range(n):
        for end in range(start, n):
            if prefix[end + 1] - prefix[start] == target:
                count += 1
                result.append(arr[start:end + 1])

    return count, result
# #start
# 0 to 5 - end 0 to 5
# prefix[0+1]=1 - prefix[start]=0  == target . no
# prefix[1+1]=3 - prefix[start]=0  == target . no
# prefix[2+1]=6 - prefix[start]=0  == target . no
# prefix[3+1]=4 - prefix[start]=0  == target . no

# start = 1
# 0 to 5 - end 0 to 5
# prefix[0+1]=1 - prefix[start]=1  == target . no
# prefix[1+1]=3 - prefix[start]=1  == target . no
# prefix[2+1]=6 - prefix[start]=1  == target . yes
# prefix[3+1]=8 - prefix[start]=1  == target . no
# prefix[4+1]=13 - prefix[start]=1  == target . no
# start = 2
# 0 to 5 - end 0 to 5
# prefix[0+1]=1 - prefix[start]=3  == target . no
# prefix[1+1]=3 - prefix[start]=3  == target . no
# prefix[2+1]=6 - prefix[start]=3  == target . no
# prefix[3+1]=8 - prefix[start]=3  == target . yes
# prefix[4+1]=13 - prefix[start]=3  == target . 
# start = 3
# 0 to 5 - end 0 to 5
# prefix[0+1]=1 - prefix[start]=6  == target . no
# prefix[1+1]=3 - prefix[start]=6  == target . no
# prefix[2+1]=6 - prefix[start]=6  == target . no
# prefix[3+1]=8 - prefix[start]=6  == target . no
# prefix[4+1]=13 - prefix[start]=6 == target . no
# start = 4
# 0 to 5 - end 0 to 5
# prefix[0+1]=1 - prefix[start]=8  == target . no
# prefix[1+1]=3 - prefix[start]=8  == target . no
# prefix[2+1]=6 - prefix[start]=8  == target . no
# prefix[3+1]=8 - prefix[start]=8  == target . no
# prefix[4+1]=13 - prefix[start]=8 == target . yes
# start = 5
# 0 to 5 - end 0 to 5
# prefix[0+1]=1 - prefix[start]=13  == target . no
# prefix[1+1]=3 - prefix[start]=13  == target . no
# prefix[2+1]=6 - prefix[start]=13  == target . no
# prefix[3+1]=8 - prefix[start]=13  == target . no
# prefix[4+1]=13 - prefix[start]=13 == target . 
# prefix[5+1]= - prefix[start]=13 == target . yes

# all count if continue = 3
# Example
arr = [1, 2, 3, 2, 5]
target = 5
count, subarrays = subarrays_with_sum(arr, target)
print("Count:", count)
print("Subarrays:", subarrays)
 