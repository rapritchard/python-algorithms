""" 
EXPONENTS
An exponent indicates how many times a number is to be multiplied by itself.

For example: 53 = 5 * 5 * 5

Sometimes exponents are also written using the caret symbol (^):

5^3 = 53

EXPONENTS IN PYTHON
We can calculate exponents in Python using the ** operator. (Why not the ^ operator? Blame Fortran.) 

square = 2 ** 2
# square = 4

cube = 2 ** 3
# cube = 8

In the social media industry, there is a concept called "spread" - it refers to how much a post spreads 
due to "reshares" after all of the original author's followers see it. 
As it turns out, social media posts spread at an exponential rate! 
We've found that the estimated spread of a social post can be calculated using the following formula:

estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )

In the formula above, average_audience_followers refers to an average calculated from each number 
within the audiences_followers argument - which is a list containing the individual follower counts of the author's followers. 
For example, if audiences_followers = [2, 3, 2, 19], then:

the author has 4 total followers
each follower has their own 2, 3, 2, and 19 followers, respectively.
"""

def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return None

    followers = 0
    for audience in audiences_followers:
        followers += audience

    return (followers / len(audiences_followers)) * (len(audiences_followers) ** 1.2)