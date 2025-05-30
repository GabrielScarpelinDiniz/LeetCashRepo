def allUntilFinalIsZero(nums, i):
    current = i
    while current < len(nums):
        if nums[current] != 0:
            return False
        current += 1
    return True
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        last_zero_at_index = -1
        while i < len(nums):
            if nums[i] == 0 and i + 1 < len(nums) and (i + 1 < last_zero_at_index or last_zero_at_index == -1):
                current = i
                aux_idx = current + 1
                if (last_zero_at_index == -1):
                    while aux_idx < len(nums):
                        nums[current], nums[aux_idx] = nums[aux_idx], nums[current]
                        current += 1
                        aux_idx = current + 1
                    last_zero_at_index = current
                    i -= 1
                else:
                    while aux_idx < last_zero_at_index:
                        nums[current], nums[aux_idx] = nums[aux_idx], nums[current]
                        current += 1
                        aux_idx = current + 1
                    last_zero_at_index = current
                    i -= 1
            i += 1
        return nums
