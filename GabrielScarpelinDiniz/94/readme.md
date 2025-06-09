# Problem 94

> Given the root of a binary tree, return the inorder traversal of its nodes' values.

# How does I solve the problem?

I use a recursive function that call yourself if the left children first and then, the right child. In the middle of the stack (call the function with the left child and right, we add the result in a list because is inorder).
