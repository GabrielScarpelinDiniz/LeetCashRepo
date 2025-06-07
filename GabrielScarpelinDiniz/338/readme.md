# Problem 338

> Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# How does I solve the problem?

The logic is simple, we create a loop for, starting from zero and going to n, and then I take the i number from the loop, convert the number to binary using bin() from python, then I take the binary string (returned by bin) and convert into decimal, in the decimal I can take each digit and sum to return the array if the sum of each bit sum of $$n_i$$.
