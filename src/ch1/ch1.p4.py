""" 
ALGORITHMS CAN BE SIMPLE
"Algorithm" seems like a big scary word, but it really just means "well-written instructions". 
For example, a recipe for baking a cake is an example of an algorithm!

Take a look at the following algorithm for adding two numbers. It might be the simplest algorithm I can think of:

Start with input variables "a" and "b"
Add "a" and "b" using the + operator, and assign the result to a new variable, "sum"
Return the "sum" variable
"""

def sum(nums):
    if not nums:
        return None

    total = 0
    for num in nums:
        total += num
    return total