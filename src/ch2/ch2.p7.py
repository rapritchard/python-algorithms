import math

""" WHAT IS A LOGARITHM?
A logarithm is the inverse of an exponent.

24 = 16

log216 = 4

"log216" can be read as "log base 2 of 16", and means "the number of times 2 must be multiplied by itself to equal 16".

"log216" can also be written as log2(16)

Some more examples:

log2(2) = 1
log2(4) = 2
log2(8) = 3
log2(16) = 4
log2(32) = 5
log10(100) = 2
log10(1000) = 3
log10(10000) = 4
LOGS (LOGARITHMS) IN PYTHON
Just import the math library and use the math.log() function.

import math

print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")
# Logarithm base 2 of 16 is: 4.0

ASSIGNMENT
We want to be able to give our influencers a simple "influencer score". It will be a small number, 
like less than 100. This will make it easier to "rank" them against each other in terms of how many people they are "influencing".

Complete the get_influencer_score function. The formula for an influencer score is:

average_engagement_percentage * log2(num_followers) """

import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)