class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        compare = idx + 1
        max_diff = 0
        while idx < len(nums):
            if compare == len(nums):
                sub = abs(nums[idx] - nums[0])
            else:
                sub = abs(nums[idx] - nums[compare])

            if sub > max_diff:
                max_diff = sub
            idx += 1
            compare = idx + 1
        return max_diff
