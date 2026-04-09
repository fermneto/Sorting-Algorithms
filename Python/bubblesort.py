def bubble(A):
    # Repeat n-1 passes through the list, to verity every index but the last one
    for i in range(len(A) - 1):

        # Each pass compares adjacent elements
        for j in range(len(A) - 1):

            # Swap neighbors if they are out of order
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    return A
  
L = [73, 12, 45, 98, 6, 34, 81, 27, 59, 90]
print(bubble(L))