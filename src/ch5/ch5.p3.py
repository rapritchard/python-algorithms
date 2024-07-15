""" REDUCTION TO P
Let's take an exponential time algorithm and rewrite it to run in polynomial time!

The Fibonacci sequence is a sequence of numbers where each number is the sum of the two numbers before it. Like this:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Copy icon
We want a function that, given an index in the sequence, returns the Fibonacci number at that index. For example:

fib(0) -> 0
fib(1) -> 1
fib(2) -> 1
fib(3) -> 2
fib(4) -> 3
fib(5) -> 5
fib(6) -> 8
fib(7) -> 13
Here are the implementation details to do it in polynomial time:

The input n represents the index of the desired Fibonacci value
Initialize three values. One will hold the current value, 
one will hold the parent value (1 before), and one will hold the grandparent value (2 before the current). 
You'll need to hard-code the first two values of the sequence. grandparent=0 and parent=1
Write a loop that iterates n-1 times. (For example, the loop should not repeat when n=2.)
Inside the loop update the current based on the parents, then update the parents to their appropriate values.
Return the current value once the loop completes
ASSIGNMENT
Our data scientists at Socialytics have found that the growth of the average influencer's 
follow count is roughly the same growth rate as the Fibonacci sequence! In other words, 
after 6 weeks of good Instagram posts, the average influencer will have 8 followers. 
After 7 weeks, 13 followers, and so on.

The trouble is, our current implementation of the fib function takes so long (exponential time!) 
to complete that when our influencers navigate to their analytics page it often never completes loading!

Adjust the fib function using the given algorithm to achieve polynomial runtime. """

def fib(n):
    if n <= 1:
        return n
    
    current = 0
    parent = 1
    grandparent = 0

    for i in range(n-1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current