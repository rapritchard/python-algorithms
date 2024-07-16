""" TRAVELING SALESMAN PROBLEM - VERIFY
We know that TSP takes factorial time to solve. 
The reason is that we need to try every permutation of all the possible cities. 
For example, given 4 cities, A, B, C, D, we need to try:

A,B,C,D
B,A,C,D
C,A,B,D
A,C,B,D
B,C,A,D
C,B,A,D
C,B,D,A
B,C,D,A
D,C,B,A
C,D,B,A
B,D,C,A
D,B,C,A
D,A,C,B
A,D,C,B
C,D,A,B
D,C,A,B
A,C,D,B
C,A,D,B
B,A,D,C
A,B,D,C
D,B,A,C
B,D,A,C
A,D,B,C
D,A,B,C

That's 4! or 4*3*2*1 or 24 permutations.

TSP IN NP
Even though it takes factorial time to solve TSP, TSP is in NP because we can verify a solution much faster. 
Let's write a TSP verifier!

ASSIGNMENT
Complete the verify_tsp function by implementing the algorithm below. Notice that it runs in polynomial time.

PSEUDOCODE: VERIFY_TSP(PATHS, DIST, ACTUAL_PATH)
INPUTS
paths: A matrix where each point represents the distance between the two cities. 
For example, paths[cityA][cityB] holds the distance from cityA to cityB. paths[cityA][cityB] = paths[cityB][cityA]
dist: The distance we are trying to find a path shorter than
actual_path: The path we are trying to verify
OUTPUT
True if the distance of the path is actually shorter than dist. False otherwise.

ALGORITHM
Loop over each city in the actual path
Sum the distance between each city in the actual path
If the sum is less than dist, return True, otherwise return False """
def verify_tsp(paths, dist, actual_path):
    total_distance = 0
    for i in range(1, len(actual_path)):
        total_distance += paths[actual_path[i-1]][actual_path[i]]

    return total_distance < dist