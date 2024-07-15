""" QUICK SORT
DESCRIPTION
Quick sort is an efficient sorting algorithm that's widely used in production sorting implementations. 
Like merge sort, quick sort is a divide and conquer algorithm.

DIVIDE
Select a pivot element that will preferably end up close to the center of the sorted pack
Move everything onto the "greater than" or "less than" side of the pivot
The pivot is now in its final position
Recursively repeat the operation on both sides of the pivot
CONQUER
The array is sorted after all elements have been through the pivot operation
VISUALS
The quick_sort algorithm is recursive. And it works in the following way:

Select a "pivot" element - We'll arbitrarily choose the last element in the list
Move through all the elements in the list and swap them around until all the 
numbers less than the pivot are on the left, and the numbers greater than the pivot are on the right
Move the pivot between the two sections where it belongs
recursively repeat for both sections

ASSIGNMENT
We now have two sorting algorithms on our Socialytics backend! 
It is a bit annoying to maintain both in the codebase. 
Quicksort is fast on large datasets just like merge sort, 
but is also lighter on memory usage. Let's use quick sort for both follower count and influencer revenue sorting!

Complete the quick_sort and partition functions according to the given algorithms.

Note: The process is started with quick_sort(A, 0, len(A)-1)

PSEUDOCODE: QUICK_SORT(NUMS, LOW, HIGH)
If low is less than high:
Partition the input list using the partition function
Recursively call quick_sort on the left side of the partition
Recursively call quick_sort on the right side of the partition
PSEUDOCODE: PARTITION(NUMS, LOW, HIGH)
Set pivot to the element at index high
Set i to low
For each index (j) from low to high
If the element at index j is less than the pivot:
Swap the element at index i with the element at index j
Increment i by 1
Swap the element at index i with the element at index high
Return the index i """

def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)

        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
