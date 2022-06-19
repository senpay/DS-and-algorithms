# Overview
This repository has implementation of various sorting algorithms, as well as some information related to them.
Sorting is the process of placing elements from a collection in some order. For example, a list of words could be sorted alphabetically or by length.

Sorting algorithms demonstration: [https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)

### Selection sort

- Run through the collection that has to be sorted
- Select the next value (for example, minimum if sorting in ascending order)
- List/collection is broken into a sorted and not sorted parts
- Found minimum (or maximum) element just swapped with the element “occupying” its place
- Selection sort is often better than bubble sort

[Implementation:](selection_sort.py)

### **Insertion sort**

- We begin by assuming that a list with one item (first one) is already sorted
- On each pass, we compare every item with “already sorted” sublist
- Then we insert item into “sorted” list, shifting items from sorted list right, if necessary
    - When we reach a smaller item or the end of the sorted sublist, current item can be inserted

[Implementation:](insert_sort.py)

### **Bubble sort**

- Run through the collection, comparing every two adjacent elements with each other
- If elements are in wrong order - they are swapped
- The algorithm continues until there’s a full collection run-through w/o swaps
- Bubble sort may be very efficient if collection is already sorted - having O(N) best case complexity!

[Implementation:](bubble_sort.py)

### **Quick sort**

- Worst-case complexity: O(N$^2$)
- Best-case complexity: O(N log(N))
- Uses divide and conquer approach
- Select “pivot” - an element to be used for comparison
    - Median of three - is an approach for selecting pivot
    - Choose first, middle and last elements
    - Choose a median value of them
- Split collection into two sub-collections (this is done “in place”, w/o using another collection):
    - Elements bigger than “pivot” would go to the right collection
    - Elements smaller than “pivot” would go to the left collection
- Repeat recursively for every sublist
- Does not use additional storage (in contrast with merge sort)

[Implementation:](quick_sort.py)

### **Merge sort**

- Uses divide and conquer approach
- If the list has 0 or 1 element - consider this sorted
- If it is not - split the list into two sublists and sort them recursively
- Finally, merge sorted sublists
    - Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list
- Time complexity - O(N log(N)) (the only algorithms that **guarantees** O(N log(N)) worst-case complexity.
- O(N) space complexity

[Implementation:](merge_sort.py)