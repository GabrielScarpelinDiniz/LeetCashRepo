# Problem 109

> Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# How the problem works?

We will receive a sorted linked list, and transform this linked list in a heighted binary search tree.

# How I solve the problem?

First, I transform the linked list in a common array with the elements sorted in the same order. It is important because work with array is more easy, access specific elements that we want can be doed in O(1). Sequentially, I'm using the divide and conquer approach. The first method that I tried was take the left elements in order (middle to 0) and the right elements (last element to middle). This approach will generate a **valid binary search tree** however this binary search tree was not be heighted balanced.

After this approach, I try an approach similarly the merge sort algorithm. In the previous step, how I decide that 0 is the best element to root? I take the middle. So is this that I made, I divide the problem in subproblems treating each node "as the root". Doing this I can do a simple algorithm that will going take the middle of each piece of subarrays and the current node as the root of my first approach.
