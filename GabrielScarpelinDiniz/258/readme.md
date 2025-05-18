# Problem 258

> Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# How does the Problem works?

Its a little bit hard to understand since the begin. Imagine that we have the number 38, the sum of each digit is 11, which have 2 digits too. So, we repeated this step until we get a number lower than 10 (one digit) or biggest/equal than 0.

# How did I solve the problem?

First, I transform the number in string (is more easy get each digit from a number that is string when compared to a int number (we can use the split, list and many other options)). Then, I compute the sum of each digit, if this sum is biggest than 10, we repeate the process. The verification about 0 is only to bring the initial case (first loop, because in reality, doesnt matters).
