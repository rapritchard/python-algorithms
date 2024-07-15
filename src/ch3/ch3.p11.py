""" ORDER 1
O(1) means that no matter the size of the input, 
there is no growth in the runtime of the algorithm. 
This is also referred to as a "constant time" algorithm.

In Python, the dictionary data structure offers the ability to look items up by key, 
which is an operation that is independent of the size of the dictionary. 
In other words, dictionary lookups are O(1).

ASSIGNMENT
We need to be able to search our Socialytics user base more quickly! 
Our users are complaining that the search bar is painfully slow. 
You'll notice that if you run the code in its current state, it will take a very long time.

The find_last_name function takes names_dict, a dictionary of first_name -> last_name. 
It also accepts a first_name. If first_name is a key in the dictionary, 
find_last_name returns the associated last name. 
If the key is not found, it returns None. 
Make sure you handle the case where the first_name is not in the dictionary!

Write the function so that it runs quickly! It should be O(1). """
def find_last_name(names_dict, first_name):
    return names_dict.get(first_name)