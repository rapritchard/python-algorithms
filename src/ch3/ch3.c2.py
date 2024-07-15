""" REMOVE DUPLICATE ELEMENTS
We're interested in showing the unique follower counts of all of an influencer's followers.

ASSIGNMENT
Complete the remove_duplicates function. 
It takes a list of integers nums and returns a new list of integers. 
The returned list of integers should consist of all the unique follower counts in nums without any duplicates.

We want to preserve the order of the list so be careful when using a set! """
def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
