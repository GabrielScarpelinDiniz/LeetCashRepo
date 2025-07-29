class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cont = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (abs(nums[i] - nums[j]) == k):
                    cont += 1
        
        return cont