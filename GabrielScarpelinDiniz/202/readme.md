# Problem 202

> Write an algorithm to determine if a number n is happy.

> A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

> Return true if n is a happy number, and false if not.

# How does I solve the problem?

First, I implemented it using a recursive approach by creating a function that calls itself. This function takes two arguments: the current number in the recursion and a set. The set is a collection of elements that do not repeat and allows fast access to its contents. In each recursive step, the function extracts the digits of the number, squares each digit, and sums the results. If the sum equals one, the number is a happy number. If the number has already appeared before (it's in the set), it means we're in a cycle, so we return false. If neither condition is met, we add the number to the set and call the function recursively with the new sum.
