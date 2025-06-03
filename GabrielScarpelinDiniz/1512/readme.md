# Problem 1512

> Given an array of integers nums, return the number of good pairs.

> A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# How does I solve the problem?

I iterate over the array two times 0...n, each index called i, and for each element a iterate a second time i + 1...n. Then, I verify if the number nums[i] and nums[j] its equal, if true, I add one in a count variable, then I return the result
