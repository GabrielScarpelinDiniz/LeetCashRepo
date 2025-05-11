# Problem 35

> Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

# How the problems works?

We need to search if an element exists on a sorted array, if the target element doesnt exists, we need to find the index where the element need to be inserted. The algorithm must be O(log n)

# How I solve the problem?

I've implement a binary search at the array, if an a extra avaliation that follows the pattern: If the target is greater than the middle element and the target is lower than the next element of the middle, this means that our element was not in the array, and need to be between these two numbers. And the same logic as applied if the element if lower, but at this case we verify if the previous element of the middle are lower than the target.
