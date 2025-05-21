# Problem 3427

> You are given an integer array nums of size n. For each index i where 0 <= i < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).

> Return the total sum of all elements from the subarray defined for each index in the array.

# How does the problem works?

We need to take the start, the end (that is i) and take a subarray nums[start...i] and return the sum of this subarray.

# How did I solve the problem?

To solve the problem, first I create a loop, taking the start index, the start index is defined by max between 0 and i - nums[i], and the end index will be i + 1 (because the inline slice methods "ends" at endIdx excluding the end.). Then, I need to calculate the sum of this subarray and the sum of the sum of subarrays will be the final result
