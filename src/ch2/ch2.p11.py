""" 
FACTORIALS
In math, the factorial of a positive integer n, written n!, is the product of all positive integers less than and equal to n.

5! = 5 * 4 * 3 * 2 * 1

The results of a factorial grow even faster than exponentiation!

n! grows faster than 2^n:

n!	2^n
2	2	4
3	6	8
4	24	16
5	120	32
6	720	64
ASSIGNMENT
Socialytics allows influencers to schedule Instagram posts to be published in the future. 
We've found that the order in which the posts are published drastically affects their performance. 
Complete the num_possible_orders function. 
It takes as input the number of posts an influencer has in their schedule and returns the 
total number of possible orders in which we could publish the posts. 
"""

def num_possible_orders(num_posts):
    possible_orders = 1
    for num in range(2, num_posts + 1):
        possible_orders *= num
    return possible_orders

