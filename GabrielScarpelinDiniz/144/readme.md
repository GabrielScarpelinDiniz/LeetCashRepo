# Problem 144

> Given the root of a binary tree, return the preorder traversal of its nodes' values.

# How does I solve the problem?

To solve the problem, I use recursion, each current node verify if each children (starting from left, because we want the preorder), if the children are not null, we call the function again with the children, always left first after right. The algorithm is really simple like this, I append each current val in a list to the output.
