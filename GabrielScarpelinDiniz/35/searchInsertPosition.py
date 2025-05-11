class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        middle = len(nums) // 2
        startIdx = 0
        endIdx = len(nums) - 1

        while startIdx <= endIdx:
            middle = (startIdx + endIdx) // 2
            if target > nums[middle]:
                startIdx = middle + 1
                endIdx = endIdx
                if middle + 1 < len(nums):
                    if nums[middle + 1] > target:
                        return middle + 1
                elif middle >= len(nums) - 1:
                    return middle + 1
            elif target < nums[middle]:
                startIdx = startIdx
                endIdx = middle - 1
                if middle - 1 >= 0:
                    if nums[middle - 1] < target:
                        return middle
                else:
                    if nums[middle] > target:
                        return middle
                    else:
                        return middle + 1
            else:
                return middle
