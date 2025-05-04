# Problem 27

> Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

> Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

> Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.

> Return k.

# How the problem works?

We need to search for a value in the array and remove all occurrences for that value. In the final, we need to return k (new length of the array)

# How I solve the problem?

It's a easiest problem to solve. We need to iter in the array, verify its an element its equal that the searched value, if its equal we need to remove the element, recalcule the new size and decrement one in the iterator - because we remove an element... It's simple, and easy to solve.
