def merge(A):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(A) <= 1:
        return A

    # Divide the list into two halves
    AL, AR = [], []
    for i in range(len(A)):
        if i < len(A) // 2:
            AL.append(A[i])
        else:
            AR.append(A[i])

    # Recursively sort each half
    AL = merge(AL)
    AR = merge(AR)

    # Merge the two sorted halves back into A
    return combine(AL, AR, A)


def combine(Left, Right, Original):
    lsize = len(Original) // 2          # Size of the left half
    rsize = len(Original) - lsize       # Size of the right half
    i, l, r = 0, 0, 0

    # Compare elements from both halves and place the smaller one next
    while l < lsize and r < rsize:
        if Left[l] < Right[r]:
            Original[i] = Left[l]
            l += 1
        else:
            Original[i] = Right[r]
            r += 1
        i += 1

    # Append any remaining elements from the left half
    while l < lsize:
        Original[i] = Left[l]
        i += 1
        l += 1

    # Append any remaining elements from the right half
    while r < rsize:
        Original[i] = Right[r]
        i += 1
        r += 1

    return Original

L = [7, 8, 5, 9, 4]
print(merge(L))