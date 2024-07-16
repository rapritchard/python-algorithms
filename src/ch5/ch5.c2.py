""" TRAVEL TIME LIMIT
Socialytics is planning a campaign where influencers are given a time limit 
to visit as many countries as possible. 
However, the travel time between countries follows an exponential growth pattern. 
This means that the more countries influencers visit, the longer it takes to travel to the next one. 
It's a small growth factor (<2) but it's still exponential.

It's a bit strange, we figure it's because they take more and more time lollygagging in each country for pleasure.

ASSIGNMENT
Write a function num_countries_in_days that takes a maximum number of days max_days 
and a time increase factor factor, 
then returns the number of countries an influencer can visit within that time limit.

Influencers start by spending 1 day in the first country. 
For the next visit and every visit after, 
the time factor is applied to the time in the current country to determine the time in the next country. 
Partial visits are not allowed and the cumulative time traveling cannot exceed the max_days.

For example:

- Max days: 2
- Time factor: 1.2
Countries visited: 1
=====================================
- Max days: 3
- Time factor: 1.2
Countries visited: 2
 """
def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while time_left >= time_in_country:
        time_left -= time_in_country
        time_in_country *= factor
        count += 1
    return count