# Problem 26

> Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

> Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

> Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.

> Return k.

# How the problem works?

We need to remove all duplicates elements in the array and return the new length of the array (k)

# How I solve the Problem

First, I create a Hashmap, containing the numbers that was appeared on the array. If the number was appears on the array, we remove the number, recalculate the new length of the array and subtract one from the index (because and was removed). Its a very simple problem to solve
