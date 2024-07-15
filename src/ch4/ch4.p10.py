""" INSERTION SORT
Insertion sort builds a final sorted list one item at a time. 
It's much less efficient on large lists than more advanced algorithms like quicksort or merge sort.
ASSIGNMENT

We have another screen in the Socialytics dashboard where our users want to sort their affiliate deals by revenue. 
None of our users have more than a couple hundred affiliate deals, 
so we don't need an n * log(n) algorithm like merge sort. 
In fact, insertion_sort can be faster than merge_sort, and uses less of our server's memory when list sizes are small.

Complete the insertion_sort function according to the given algorithm.

PSEUDOCODE
For each index in the input list:
Set a j variable to the current index
While j is greater than 0 and the element at index j-1 is greater than the element at index j:
Swap the elements at indices j and j-1
Decrement j by 1
Return the list
TIP
In some languages you need to use a temp variable to swap values, but in python you can do that in a single line:

a = 5
b = 3
a, b = b, a
print(a)
# 3
print(b)
# 5 """

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums