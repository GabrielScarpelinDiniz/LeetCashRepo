class Solution(object):
    def missingNumber(self, nums):
        i=0
        while i<(len(nums)+1):
            if i not in nums:
                return i
            i+=1
        