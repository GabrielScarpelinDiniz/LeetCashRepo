class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        for x in range(1, len(nums)):
            if nums[x] == nums[x -1]:
                return True
        return False