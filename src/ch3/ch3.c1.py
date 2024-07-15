""" NAME COUNT
In Socialytics, we process tons of user's names. They are often structured as lists of lists. 
For example, a separate list of users for each influencer's followers.

ASSIGNMENT
Complete the count_names function.

It should iterate over all the names in the nested list_of_lists and count all the instances of target_name, 
then return the count.

OBSERVE
What's the time complexity of your solution? It should be O(n) on the total number of names, 
but O(mn) if you consider m to be the number of lists and n to be the average length of a list. """

def count_names(list_of_lists, target_name):
    count = 0
    for list in list_of_lists:
        for name in list:
            if target_name == name :
                count += 1
    return count
