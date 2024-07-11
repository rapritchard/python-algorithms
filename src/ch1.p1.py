def find_minimum(nums):
    if not nums:
        return None
    min = float("inf")
    
    for num in nums:
        if (num < min):
            min = num
    return min