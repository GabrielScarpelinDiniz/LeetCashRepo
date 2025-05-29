# Problem 2894

You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.

# How does I solve the problem?

I just create a loop, checking if the number is divisible by n and not, and sum a variable with is, and another if is not. In the final I return the first sum (non-divisible) minus the second sum.
