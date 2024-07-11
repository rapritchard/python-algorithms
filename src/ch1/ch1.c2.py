""" 
MEDIAN
A median is often more useful than an average when the data set contains outliers. 
For example, if you want to know the typical salary of a software engineer, the median can be a better measure than the average, 
because the average can be skewed by a few people who make a lot of money.

At Socialytics, we want to show our influencers the median follower count of the people they follow.
 """
def median_followers(nums):
    if not nums:
        return None
        
    sorted_nums = sorted(nums)
    list_len = len(sorted_nums)
    mid = list_len // 2

    if list_len % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]