class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        
        return len(arr)
        