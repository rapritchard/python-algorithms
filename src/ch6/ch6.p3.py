""" TRAVELING SALESMAN PROBLEM
A famous example of a problem in NP is the Traveling Salesman Problem, also known as TSP.

The version of the problem that we will solve can be stated:

Given a list of cities, the distances between each pair of cities, 
and a total distance, is there a path through all the cities that is less than the distance given?

For example, with the above graph, the problem could be, "Is there a way to travel through A, B, C, and D 
in less than a distance of 67?" The answer would be "yes" by way of A -> B -> D -> C

ASSIGNMENT
Our Socialytics Instagrammers need to travel to trade shows to shill their sponsor's products! 
Since none of them trust Google Maps, they want to put in their proposed route to Socialytics, 
and our app will tell them if their route is short enough to be worth their time.

Complete the tsp function by performing a brute-force search using the provided algorithm. 
The brute-force search will, unfortunately, take factorial time, O(n!), 
because you will need to try all possible paths and keep track of the shortest.

There is a helper function, permutations(), provided for you that will provide all possible permutations of a list.

PSEUDOCODE: TSP(CITIES, PATHS, DIST)
INPUTS
cities: A list of city identifiers (integers 0-n)
paths: A matrix where each point represents the distance between the two cities. 
For example, paths[cityA][cityB] holds the distance from cityA to cityB. paths[cityA][cityB] = paths[cityB][cityA]
dist: The distance we are trying to find a path shorter than
OUTPUT
True if there is a path shorter than dist. False otherwise.

ALGORITHM
Use the permutations function to get the matrix of all possible paths through the given cities. 
For example, permutations([1,2,3]) would result in:
[
    [1, 2, 3],
    [2, 1, 3],
    [3, 2, 1],
    [2, 3, 1],
    [3, 1, 2],
    [1, 3, 2]
]

Where the first path, [1, 2, 3] represents moving from city 1 -> city 2 -> city 3

Loop over each resulted permutation
Loop over each city in the path keeping a sum of all the distances between each city.
If the total distance in the path is less than the given dist return True
If no short paths were found, return False """

def tsp(cities, paths, dist):
    permutations_of_cities = permutations(cities)

    for current_path in permutations_of_cities:
        total_distance = 0
        for i in range(1, len(current_path)):
            total_distance += paths[current_path[i - 1]][current_path[i]]
        if total_distance < dist:
            return True
    return False


# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
