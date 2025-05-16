# Problem 23

> You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

> Merge all the linked-lists into one sorted linked-list and return it.

# How the problem works?

We will receive a list containing k roots elements of a linked list (sorted). We need to return the final sorted linked list merging that linked lists

# How I solve the problem?

I use the same logic that we use to merge a two sorted lists. I create k pointers (for each k element of linked list), compare the k current elements for each pointers, take the lower pointer and advance one step to that pointer. I use some approaches, like delete unused pointers because I was taking time limit when submitting. My algorithm was taking worst runtime at leetcode platform, if someone can help me improve this time looking to my code.
