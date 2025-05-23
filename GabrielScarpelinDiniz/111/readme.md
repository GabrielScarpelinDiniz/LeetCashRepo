# Problem 111

> Given a binary tree, find its minimum depth.

> The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

> Note: A leaf is a node with no children.

# How did the problem works?

To solve the problem we need to find the first node that has no children (minimum depth).

# How does I solve the problem?

First, I implement a BFS (Breadth First Search), this travel by the tree depth by depth. This is perfect to find our minimum depth. I create a new structure to save the depth along the tree. This able me to store the depth (that is a challenge in the bfs). I just return when we find a node that have no childrens. The implementation of a binary tree is pretty simple, we need a queue, and going add each children of the current element on the queue.
