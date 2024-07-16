import math

""" PRIME FACTORIZATION
Let's solve a commonly misunderstood problem in computer science - finding the prime factors of a number. 
Almost all modern cryptography, including your browser's HTTPS encryption, 
is based on the fact that prime factorization is slow. You'll learn why that is later in our Cryptography course.

For now, let's focus on the speed of factorization, and how it relates to the P and NP classes.

Finding a number's prime factors is an algorithm in the NP class.

When given two primes and their product, all we need to do is a simple multiplication step to verify correctness. (polynomial time)
Given just a number, finding its prime factors is a much more difficult problem. (exponential time is the best we know of)
The trouble is that no one has formally proven that there is not a polynomial time algorithm for finding prime factors. 
So, we're technically unsure if the problem is in P or if it's NP-complete.

Either way, let's build it!

PRIME FACTORS ALGORITHM
Given a large number, return a list of all the prime factors.

prime_factors(8) -> [2, 2, 2]
prime_factors(10) -> [2, 5]
prime_factors(24) -> [2, 2, 2, 3]
Divide n by two as many times as you can do so evenly (no remainder). For each division, append a 2 to the list of prime factors.
At this point, n must be odd. Start a loop that iterates over all odd numbers from 3 to the square root of n inclusive. Use math.sqrt().
For each number i, if n can be divided evenly by i, then divide n by i and append i to the list. 
Repeat this (nested loop) until i can't divide evenly into n, then move on to the next i.
If n is still greater than 2 after that loop, it must still be prime, so just append it to the list.
Return the list of primes, ordered from least to greatest.
ASSIGNMENT
Complete the prime_factors function according to the given algorithm. Notice how the algorithm gets much slower as the size of the input (in bits) grows.

Note: The returned list should only contain ints, no floats. """

def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n /= i


    if n > 2:
        factors.append(int(n))
    
    return factors