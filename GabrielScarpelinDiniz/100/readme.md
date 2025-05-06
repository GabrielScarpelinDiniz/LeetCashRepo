# Problem 100

> Given the roots of two binary trees p and q, write a function to check if they are the same or not.

> Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# How the problem works?

We need to check if two different binary tree are equals. What is equals? All the values from root node and their childrens are equals.

# How I solve the problem?

I solve the problem using a BFS (Breadth First Search). So I implement a queue that the children of each node of each tree are added, and return false if these childrens are not equals. We do an Array of Array, where we have in the inner array the childrens of each node of each tree. And we need only to verify if are equals.
