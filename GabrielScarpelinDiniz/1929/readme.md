# Problem 1929

> Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

> Specifically, ans is the concatenation of two nums arrays.

> Return the array ans.

# How does I solve the problem?

First, I create an array filled by 0 with 2n elements where n is the number of elements in nums. Then, I use the follow rule: take the num element from nums and add in the same index of nums and add in the len(nums) + currentIdx in nums, then we will concatenate the array as the exercise ask.
