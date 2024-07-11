""" 
AVERAGE
We now need a way to show our Instagram influencers the average follower count of the people they follow. 
This will help them know if they're following people who are more or less popular than them.
"""
 
def average_followers(nums):
    if not nums:
        return None
    follower_count = 0
    for num in nums:
        follower_count += num
    return follower_count / len(nums)