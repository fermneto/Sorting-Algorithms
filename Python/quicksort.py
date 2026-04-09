def quick(A):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(A) <= 1:
        return A

    # Use the last element as the pivot
    pivot = A[len(A) - 1]

    # --- Partition step ---
    # Rearrange elements so that everything less than the pivot comes before it
    i = -1  # Starter index for the last element confirmed to be less than pivot
    for j in range(len(A) - 1):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    # Place the pivot in its final sorted position
    A[i + 1], A[len(A) - 1] = A[len(A) - 1], A[i + 1]

    # --- Split step ---
    # Collect elements to the left and right of the pivot
    p1, p2 = [], []

    for i in range(len(A)):
        if A[i] == pivot:
            break
        p1.append(A[i])

    for j in range(len(A) - len(p1) - 1):
        p2.append(A[j + i + 1])
      
    # Recursively sort each partition
    p1 = quick(p1)
    p2 = quick(p2)

    # --- Reassemble ---
    # Write sorted left partition, pivot, then sorted right partition back into A
    for i in range(len(p1)):
        A[i] = p1[i]

    A[len(p1)] = pivot

    for j in range(len(p2)):
        A[len(p1) + j + 1] = p2[j]

    return A

L = [73, 12, 45, 98, 6, 34, 81, 27, 59, 90]
print(quick(L))