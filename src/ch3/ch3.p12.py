""" ORDER LOG N
O(log(n)) algorithms are only slightly slower than O(1), 
but quite a bit faster than O(n). 
They do grow according to the input size, n, but only according to the log of the input.

O(n):

n	time
8	8 ms
64	64 ms
1024	1024 ms
1048576	1048576 ms
O(log(n)):

n	time
8	3 ms
64	6 ms
1024	10 ms
1048576	20 ms
BINARY SEARCH

A binary search algorithm is a common example of an O(log(n)) algorithm. 
Binary searches work on a sorted list of elements.

PSEUDOCODE
Given an array of n elements sorted from least to greatest, and a target value:

Set low = 0 and high = n - 1.
While low <= high:
Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
If array[median] == target, return True
Else if array[median] < target, set low to median + 1
Otherwise set high to median - 1
Return False
Because at each iteration of the search we are halving the size of the search space, 
the algorithm has a complexity of log2, or O(log(n)).

In other words, to add another step to the runtime, 
we need to double the size of the input. Binary searches are fast.

ASSIGNMENT
We have a popular Instagrammer using our Socialytics app, 
and she needs to be able to quickly search for posts from a particular day. 
This function will be the backbone of her search screen.

Complete the binary_search function. It should follow the algorithm as described above. """

def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False