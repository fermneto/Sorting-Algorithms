# 📊 Sorting Algorithms

A collection of classic sorting algorithms implemented in Python and C++. This repository serves as a study reference, with clear and readable implementations for each algorithm.

---

## Algorithms

###  Bubble Sort — `bubblesort.py` | `bubblesort.cpp`

Repeatedly compares adjacent elements and swaps them if they are out of order. The largest unsorted element "bubbles up" to its correct position on each pass.

- **Time complexity:** O(n²) average and worst case
- **Space complexity:** O(1)
- **Stable:** Yes
- **Best for:** Educational purposes; very small or nearly sorted lists

---

###  Selection Sort — `selectionsort.py` | `selectionsort.cpp`

Divides the list into a sorted and an unsorted portion. On each iteration, finds the smallest element in the unsorted portion and places it at the start of the unsorted portion.

- **Time complexity:** O(n²) in all cases
- **Space complexity:** O(1)
- **Stable:** No
- **Best for:** Small lists; situations where memory writes are expensive (performs at most n swaps)

---

###  Insertion Sort — `insertionsort.py` | `insertionsort.cpp`

Builds the sorted list one element at a time. For each new element, it shifts larger elements to the right until the correct position is found and inserts the element there.

- **Time complexity:** O(n²) average and worst case; O(n) best case (already sorted)
- **Space complexity:** O(1)
- **Stable:** Yes
- **Best for:** Small lists; nearly sorted data; online sorting (sorting as data arrives)

---

###  Quick Sort — `quicksort.py`

Selects a pivot element and partitions the list so that all elements smaller than the pivot come before it, and all larger elements come after. Recursively applies the same logic to each partition.

- **Time complexity:** O(n log n) average; O(n²) worst case (already sorted list with poor pivot choice)
- **Space complexity:** O(log n) due to recursion stack
- **Stable:** No
- **Best for:** Large datasets; general-purpose sorting; cache-efficient performance in practice

---

###  Merge Sort — `mergesort.py`

Recursively divides the list in half until each sublist has a single element, then merges the sublists back together in sorted order.

- **Time complexity:** O(n log n) in all cases
- **Space complexity:** O(n) auxiliary space
- **Stable:** Yes
- **Best for:** Large datasets; linked lists; situations where stable sorting is required; external sorting (data that doesn't fit in memory)

---

## A note on stability

A sorting algorithm is considered **stable** if it preserves the original relative order of elements that compare as equal.

This only matters when sorting objects by one of their fields — for example, a list of people sorted by age. If two people share the same age, a stable algorithm guarantees they will appear in the same order they did in the original list. An unstable algorithm may swap them arbitrarily.

For simple lists of numbers (like the examples in this repo), stability has no visible effect since equal values are indistinguishable.

---

## Complexity Summary

| Algorithm      | Best       | Average    | Worst      | Space    | Stable |
|----------------|------------|------------|------------|----------|--------|
| Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅     |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)     | ❌     |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅     |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | ❌     |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | ✅     |

---

## Requirements

**Python**
- Python 3.x
- No external dependencies

**C++**
- C++11 or later
- Any standard compiler (g++, clang++, MSVC)

## Usage

**Python**
```bash
python bubblesort.py
python selectionsort.py
python insertionsort.py
python quicksort.py
python mergesort.py
```

**C++**
```bash
g++ bubblesort.cpp -o bubblesort && ./bubblesort
g++ selectionsort.cpp -o selectionsort && ./selectionsort
g++ insertionsort.cpp -o insertionsort && ./insertionsort
```

---

## Planned Additions

- Heap Sort
- Shell Sort
- Counting Sort
- Radix Sort
- Timsort

---

*Contributions and suggestions are welcome!*
