class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                nums.pop(i)
                i -= 1
                length = len(nums)
            i += 1
        return len(nums)
