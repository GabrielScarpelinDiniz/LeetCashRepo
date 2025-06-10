class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * (len(nums) * 2)
        for idx, num in enumerate(nums):
            ans[idx], ans[len(nums) + idx] = num, num

        return ans
