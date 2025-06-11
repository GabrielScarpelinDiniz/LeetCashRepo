# Problem 222

> Given the root of a complete binary tree, return the number of the nodes in the tree.

> According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

> Design an algorithm that runs in less than O(n) time complexity.

# How does I solve the problem?

To solve the problem in O(n) time complexity, I implement a BFS (Bredth First Search), that goes level by level in the binary tree. And I implement a variable (countNodes) that count every node.
