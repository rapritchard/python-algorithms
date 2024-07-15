""" ORDER 2^N - EXPONENTIAL
O(2^n) is the first Big O class that we've dealt with that falls into the scary exponential category of algorithms.

Algorithms that grow at an exponential rate become impossible to compute after so few iterations that they are 
almost worthless in practicality.

ASSIGNMENT
At Socialytics we need to be able to compute the power set of a set of influencers. 
Something about targeting segments of an audience with ads. I don't know, I just do what I'm told.

A power set is the set of all possible subsets of a set. For example, the set {1, 2, 3} has the power set:

{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

We'll work with lists instead of sets for simplicity.

Complete the power_set function using the following algorithm:

Check if the input list is empty. If it is, return a list containing an empty list. 
(The power set of an empty set is a set containing just the empty set)
Otherwise, create an empty list to hold all the final subsets of the input list.
Recursively call power_set. Pass in all of the elements in the input set except the first one.
Iterate over the list of subsets returned from the recursive call. 
For each subset, append two new subsets to the final list of subsets:
list_with_only_the_first_item_from_input_set + subset
subset
Return the list of subsets
OBSERVE!
Notice how the power_set() function gets exponentially slower with each iteration. This is because its complexity class is O(2^n)

If we could calculate one subset per millisecond, completing the power_set() of just 25 items would take approximately 9 hours, and that's not accounting for the massive amounts of memory we would need.

40 items would take over 34 years! """
def power_set(input_set):
    if not input_set:
        return [[]]
    subsets = []
    r_subsets = power_set(input_set[1:])
    for subset in r_subsets:
        subsets.append(input_set[:1] + subset)
        subsets.append(subset)
    return subsets