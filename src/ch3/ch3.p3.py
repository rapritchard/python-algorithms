""" O(N^2) - ORDER "N SQUARED"
O(n^2) grows in complexity much more rapidly. 
For small and medium input sizes, these algorithms can still be very useful.

A common way that an algorithm will fall into the O(n^2) class is by using a nested loop, 
where the number of iterations of each loop is equal to the number of items in the input.

ASSIGNMENT
Socialytics needs search capabilities! For now, we'll build something slow but simple. 
Our users want to give us the full name of a fellow Instagrammer, 
and we need to find them by checking if their first and last names exist in our database.

Complete the does_name_exist function. 
It should loop over all of the first/last name combinations in the first_names and last_names lists. 
If it finds a combination that matches the full_name it should return True. 
If the full name isn't found, it should return False instead.

OBSERVE
When you run your completed code, notice how each successive call to does_name_exist takes quite a bit longer. 
Assuming the length of first_names and last_names is the same, 
each new name doesn't add n steps to the algorithm it adds n^2 steps.

If does_name_exist(10 first and last names) takes just 1 second to complete, 
then we can assume the following timings are roughly accurate:

does_name_exist(100 first and last names) = 100 seconds
does_name_exist(1,000 first and last names) = 10,000 seconds
does_name_exist(10,000 first and last names) = 1,000,000 seconds """

def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if full_name == f"{first_name} {last_name}":
                return True
    return False