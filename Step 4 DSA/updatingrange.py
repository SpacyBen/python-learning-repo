def rev(n,update):
    #[0,2,5,5,3]
    freq = [0] * (n+1) #[0] [2] [3][0] [-2] [-3]
    
    for l,r,val in update:
        freq[l] += val
        if r + 1 < len(freq):
            freq[r+1] -= val

    current = 0
    output = []
    for i in range(len(freq)-1):
        current += freq[i]
        output.append(current)
    return output



if __name__ == "__main__":
    n = 5
    updates = [
        (1, 3, 5),
        (2, 4, 3)
    ]

    print(rev(n,updates))