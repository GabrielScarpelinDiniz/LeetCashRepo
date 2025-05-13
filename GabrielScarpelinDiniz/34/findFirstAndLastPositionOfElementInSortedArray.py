class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        if (len(nums) == 1):
            if nums[0] == target:
                return [0,0]
            else:
                return [-1, -1]
        middle = len(nums) // 2
        startIdx = 0
        endIdx = len(nums) - 1

        targetFirstIdx = -1
        while startIdx <= endIdx and targetFirstIdx == -1:
            if target > nums[middle]:
                startIdx = middle + 1
                endIdx = endIdx
            elif target < nums[middle]:
                startIdx = startIdx
                endIdx = middle - 1
            elif target == nums[middle]:
                if middle > 0:
                    if nums[middle - 1] != target:
                        targetFirstIdx = middle
                    else:
                        startIdx = startIdx
                        endIdx = middle - 1
                else:
                    targetFirstIdx = middle
            middle = (startIdx + endIdx) // 2

        middle = len(nums) // 2
        startIdx = 0
        endIdx = len(nums) - 1

        targetSecondIdx = -1
        while startIdx <= endIdx and targetSecondIdx == -1:
            if target > nums[middle]:
                startIdx = middle + 1
                endIdx = endIdx
            elif target < nums[middle]:
                startIdx = startIdx
                endIdx = middle - 1
            elif target == nums[middle]:
                if middle < len(nums) - 1:
                    if nums[middle + 1] != target:
                        targetSecondIdx = middle
                    else:
                        startIdx = middle + 1
                        endIdx = endIdx
                else:
                    targetSecondIdx = middle
            middle = (startIdx + endIdx) // 2

        return [targetFirstIdx, targetSecondIdx]
