# Problem 938

> Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# How does I solve the problem?

To iterate by the binary search tree I use the BFS implementation, that explore the binary tree level by level. For each element, I verify if the current element is in the range (inclusive) of low and high, if its in the range, we sum to the result variable. Finally, I return the value at the final of the function.
