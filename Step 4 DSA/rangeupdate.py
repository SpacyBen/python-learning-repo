def range1(n,update):
    diff = [0] * (n + 1)
    for l,r,val in update:
        diff[l] += val
        if r + 1 < len(diff):
            diff[r+1] -= val

    current = 0
    output = []
    for i in range(n):
        current += diff[i]
        output.append(current)

    return print(output)

def range2(n,update):
    diff = [0] * (n)
    for l,r,val in update:
        for i in range(l,r):
            diff[i] += val
    return print(diff)
            



if __name__ == "__main__":
    n = 5
    updates = [
        (1, 3, 2),
        (2, 4, 3)
    ]
    range1(n,updates)
    range1(n,updates)
