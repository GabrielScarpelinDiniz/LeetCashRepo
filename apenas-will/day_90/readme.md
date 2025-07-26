## Problem: 75. Sort Colors
**Goal**: Given an integer array `nums` where 0 represents red, 1 represents white and 2 represents blue, modify the original array putting all the same colors together and in the order given previously.

## Approach
First, I define an array `count` that will keep the counting of occurrences of each element ( `count[i]` will keep how many times the element i can be found in the array. Because of the usage of an array, this method works better if the "amplitude" of the values is small, i.e. the difference between the smallest and largest value isn't large). Then, iterate over the `count` array increasing the counting each time a specific value is found. Finally, iterate over `nums` replacing the elements for the smallest index in `count` that the value in it is greater than 0.

## Complexity analysis
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$ ( $\Theta(2n)$ )
- **Space complexity**: $O(1)$
