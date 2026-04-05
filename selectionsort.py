def selection(A):
    for i in range(len(A)):

        # Assume the current position holds the minimum of the unsorted portion
        min_idx = i

        # Search for a smaller element in the remaining unsorted portion
        for j in range(len(A) - i):
            if A[j + i] < A[min_idx]:
                min_idx = j + i

        # Place the found minimum at the start of the unsorted portion
        A[i], A[min_idx] = A[min_idx], A[i]

    return A

L = [73, 12, 45, 98, 6, 34, 81, 27, 59, 90]
print(selection(L))
