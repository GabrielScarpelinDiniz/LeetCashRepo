# Problem 700

> You are given the root of a binary search tree (BST) and an integer val.

> Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# How does the problem works?

You need to find the element in a binary search tree.

# How did the problem works?

To solve the problem I implement a simple BFS. The bfs travel along the nodes and find the target value. I know that in a binary search tree, we can going to the right side to find the target node, but this is more fast to find a solution in five minutes (time that I spend to solve.)
