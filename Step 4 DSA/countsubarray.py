def count_subarrays(arr, n):
    diff = {0:1}
    count = 0
    curr = 0
    for i in arr:
        curr += i
        if (curr-n) in diff:
            count += diff[curr-n]
        diff[curr] = diff.get(curr,0) + 1
    return count
        

if __name__ == "__main__":
    print(count_subarrays([1, 2, 3, 2, 5], 5))