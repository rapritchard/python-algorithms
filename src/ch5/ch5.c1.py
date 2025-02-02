""" EXPONENTIAL GROWTH SEQUENCES
At Socialytics, we are interested in simulating the exponential growth of an influencer's followers 
over a certain period with an adjustable growth factor.

ASSIGNMENT
Complete the exponential_growth function. Given the initial followers count n, 
growth factor factor, and number of days days, 
return a list containing the exponential growth of followers for each day.

For example:

- Initial followers: 10
- Growth factor: 2
- Days: 4

Growth sequence: [10, 20, 40, 80, 160] """

def exponential_growth(n, factor, days):
    growth = [n]
    for i in range(days):
        new_followers = growth[i] * factor
        growth.append(new_followers)
    return growth