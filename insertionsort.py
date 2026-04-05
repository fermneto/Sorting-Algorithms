def insertion(A):
    # Start from index 1 since it can not be sorted from index [0-1]
    for i in range(1, len(A)):
        buff = A[i]  # Element to be inserted into the sorted portion

        # Walk backwards through the sorted portion  
        for j in range(i):
            # Shift each element one position to the right while it's greater than buff
            if A[i - j - 1] > buff:
                A[i - j - 1], A[i - j] = A[i - j], A[i - j - 1]
            else:
                # Correct position found, no need to go further
                break

    return A
  
L = [73, 12, 45, 98, 6, 34, 81, 27, 59, 90]
print(insertion(L))
