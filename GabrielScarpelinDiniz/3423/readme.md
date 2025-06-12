# Problem 3423

> Given a circular array nums, find the maximum absolute difference between adjacent elements.

> Note: In a circular array, the first and last elements are adjacent.

# How does I solve the proble?

First, I need to compare each pair on the array. For this, I create two variables: idx and compare. Idx is the current element, and compare is the next element (compared to idx). Then, I iterate by the array, verifying if the sum between nums[idx] and nums[compare] is the biggest. A corner case is when idx is the last element and we need to compare the with the first element.
