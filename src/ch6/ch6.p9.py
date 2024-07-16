""" VERIFYING SOLUTIONS
I want to circle back to this idea of "slow to solve, fast to verify".

As it turns out, even when we aren't specifically talking about P and NP, 
the concept of "slow to solve, fast to verify" is very important in real-world software. 
As a trivial example, imagine the password on an email account.

When a user inputs a password like:

p@ssword4Mi

It's easy to verify if a password matches the one we have saved on file. It's literally as easy as:

should_grant_access = user_input == saved_password

The useful bit is that it takes much longer to guess the correct key.

Note: This password example demonstrates the guess/verify concept well, 
but when it comes to storing passwords in plain text this example is very insecure. 
We'll cover how to handle passwords in a production system in a future course.

ASSIGNMENT
The influencers who use Socialytics are worried about account security. 
We've assured them that their passwords are long and strong enough, but they want data.

Complete the get_num_guesses function. It takes a password length as input and returns 
the number of guesses required to ensure that a password of that length or shorter is guessed.

THE GUESSING STRATEGY
We're assuming a brute-force guessing strategy. A guesser needs to guess all possible passwords 
up to and including the given length to ensure they find the matching one. For example:

a
b
c
...
aa
ab
ac
...
ba
bb
bd
...
aaa
aab
aac
...

Assume that only the 26 lowercase English letters can be used in passwords.

EXAMPLE INPUT/OUTPUT
length 1 = 26 guesses
length 2 = 702 guesses
length 3 = 18278 guesses """

def get_num_guesses(length):
    guess_total = 0
    for i in range(1, length + 1):
        guess_total += 26 ** i
    return guess_total