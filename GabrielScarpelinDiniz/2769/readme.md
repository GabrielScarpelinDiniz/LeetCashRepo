# Problem 2769

> Given two integers, num and t. A number x is achievable if it can become equal to num after applying the following operation at most t times:

> Increase or decrease x by 1, and simultaneously increase or decrease num by 1.

> Return the maximum possible value of x.

# How does I solve the problem?

To solve the problem, I just found a pattern in the question, we need only to take t multiply by 2 and adds the result in num. And then, we will find the max value for **x**. Its a code that can be reached in one line.
