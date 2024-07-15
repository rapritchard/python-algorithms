""" SORTING ALGORITHMS
Sorting is a very common problem in software. Imagine you are organizing books on a shelf; 
how would you explain it step by step to someone else? Sorting algorithms can be surprisingly tricky!

Fortunately, most programming languages provide their own implementation of sorting. 
In Python, for example, we can use sorted:

items = [1, 5, 3]
print(sorted(items)) # [1, 3, 5]
Copy icon
ASSIGNMENT
In Socialytics, we want to be able to sort influencers by their overall vanity. 
We define vanity using this formula:

vanity = num_bio_links * 5 + num_selfies
Copy icon
VANITY
This function should compute the vanity of an influencer and return the result.

VANITY_SORT
This function should return a list of influencers, ordered by their vanity. 
You can pass a named parameter called key to the sorted function to control what the list gets sorted by 
(hint: you already wrote this function!) """

class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

# dont touch above this line

def vanity(influencer):
    return influencer.num_bio_links * 5 + influencer.num_selfies

def vanity_sort(influencers):
    return sorted(influencers, key=vanity)
