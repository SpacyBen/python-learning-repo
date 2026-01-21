A = [2, 4, 3, 5, 1]
B = [1, 5, 2, 4, 6]
C = []
for i in range(len(A)):
    if A[i] < B[i]:
        C.append(A[i] ** 2)
    elif A[i] > B[i]:
        C.append(B[i] ** 2)
    elif A[i] == B[i]:
        C.append(A[i] + B[i])
print("Resulting list C:", C)