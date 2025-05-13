# Problem 34

> Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

> If target is not found in the array, return [-1, -1].

> You must write an algorithm with O(log n) runtime complexity.

# How the problem works?

First, the problem want that you solve the problem in O(log n), so we know that we need to implement a binary search, that find the first target on the array and the last target on the array.

# How I solve the problem?

I solve the problem applying two binary search this is O(2log n) that is equals to O(log n). To solve the problem I use the two followed strategy: If I found the target, the previous element is different? If its true, its the first element. If its not we need to continue iterating on the array to the very left. If I found the target, the next element is different? If its true, thats mean its our last element. If not, we need to iterating by the array on the very right.
