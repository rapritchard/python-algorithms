""" MERGE SORT
Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort.

DIVIDE AND CONQUER
Merge sort is a divide and conquer algorithm.:

Divide: divide the large problem into smaller problems, and recursively solve the smaller problems
Conquer: Combine the results of the smaller problems to solve the large problem
In merge sort specifically we:

DIVIDE
Divide the array into two (equal) halves
Recursively sort the two halves
CONQUER
Merge the two halves to form a sorted array

ALGORITHM
The algorithm consists of two separate functions, merge_sort and merge.

merge_sort() divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

The merge() function is used for merging two sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each have a length of 1. Those single element lists will be merged into a sorted list of length two, and we can build from there.

MERGE_SORT() IMPLEMENTATION
Input: A, a list of integers

If the length of A is less than 2, it's already sorted so return it
Split the input array into two halves down the middle
Call merge_sort() twice, once on each half
Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
MERGE() IMPLEMENTATION
Inputs: A, B. Two lists of integers

Create a new "final" list of integers.
Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other). Add those extra items to the final list.
Return the final list.
ASSIGNMENT
Our users are complaining on Socialytics that when they sort their followers by follower count, it gets really slow if they have more than 1,000 followers. Let's speed it up for them with merge sort.

Complete the merge_sort and merge functions according to the described algorithms. """

def merge_sort(nums):
    length = len(nums)
    if length < 2:
        return nums

    middle = length // 2
    left_side = nums[:middle]
    right_side = nums[middle:]

    sorted_left_side = merge_sort(left_side)
    sorted_right_side = merge_sort(right_side)

    return merge(sorted_left_side, sorted_right_side)
    


def merge(first, second):
    final_list = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final_list.append(first[i])
            i += 1
        else:
            final_list.append(second[j])
            j += 1

    while i < len(first):
        final_list.append(first[i])
        i += 1

    while j < len(second):
        final_list.append(second[j])
        j += 1
    
    return final_list
    
