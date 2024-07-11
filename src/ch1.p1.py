""" 
WHAT IS AN ALGORITHM?
An "algorithm" is simply a set of instructions to solve a particular problem. 
People use algorithms all the time, without even realizing it. 
If you've ever organized books on a shelf, packed your luggage for a trip, or followed a cooking recipe, then you've already used an algorithm!

Computers use algorithms, too. Here's an example of a simple algorithm that explains how to find the smallest number in a list:

ALGORITHM: FIND MINIMUM
Set minimum to positive infinity: float("inf").
For each number in the list nums, compare it to minimum. If num is smaller, set minimum to num.
minimum is now set to the smallest number in the list. 
"""

def find_minimum(nums):
    if not nums:
        return None
    min = float("inf")
    
    for num in nums:
        if (num < min):
            min = num
    return min