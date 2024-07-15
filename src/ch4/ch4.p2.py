""" BUBBLE SORT
In this chapter, we are going to be learning about various algorithms to sort data. 
But wait, if sorted() exists, why should we learn bubble sort?

In all seriousness, we're going over these because:

Hard things make us better engineers
It helps to see more examples of the Big O runtimes we've studied
Bubble sort is named for the way elements "bubble up" to the top of the list.

DESCRIPTION
[5, 3, 7, 8, 7] -> [3, 5, 7, 7, 8]
Bubble sort repeatedly steps through a slice and compares adjacent elements, 
swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted.

Pseudocode for bubble sort:

Procedure bubble_sort(nums):
    Set swapping to True
    Set end to the length of nums
    While swapping is True:
        Set swapping to False
        For i from the 2nd element to end:
            If the (i-1)th element of nums is greater than the ith element:
                Swap the (i-1)th element and the ith element of nums
                Set swapping to True
        Reduce end by one
    Return nums
End Procedure

ASSIGNMENT
While our avocado toast influencers were happy with our search functionality, now they want to be able to sort their followers by follower count. Bubble sort is a straightforward sorting algorithm that we can implement quickly, so let's do that!

Complete the bubble_sort function according to the described algorithm above. """

def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums