class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found_elements = {}

        length = len(nums)
        i = 0
        while i < length:
            if found_elements.get(nums[i]) == None:
                found_elements[nums[i]] = True
            else:
                nums.pop(i)
                length = length - 1
                i = i - 1
            i = i + 1

        return len(nums)
