def good1(nums):
    output = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                output.append((i,j))
    
    return output

def good2(nums):
    n = len(nums)
    good_pairs = 0
    dik = {}
    for i in range(n):
        dik[nums[i]] = dik.get(nums[i],0) + 1
        

    for i,num in enumerate(nums):
        dik[num] -= 1
        good_pairs += dik[num]
        

    return good_pairs

def good3(nums):
    freq = {}
    count = 0
    
    for num in nums:
        if num in freq:
            count += freq[num]   # add how many we've already seen
            freq[num] += 1
        else:
            freq[num] = 1
    return count

def good4(nums):
    freq = {}        # number -> list of indices seen
    output = []

    for i in range(len(nums)):
        num = nums[i]

        if num in freq:
            # create pairs with previous indices
            for prev_index in freq[num]:
                output.append((prev_index, i))
            freq[num].append(i)
        else:
            freq[num] = [i]

    return output


def good5(nums):
    freq = {}
    output = []

    for i in range(len(nums)):
        num = nums[i]

        if num in freq:
            for prev in freq[num]:
                output.append((prev,i))
            freq[num].append(i)
        else:
            freq[num] = [i]
    return output




nums = [1,2,3,1,1,3]
print(good1(nums))
print(good2(nums))
print(good3(nums))
print(good4(nums))
print(good5(nums))