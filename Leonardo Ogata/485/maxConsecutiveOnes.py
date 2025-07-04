class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        current = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            elif nums[i] == 0:
                if current > ans:
                    ans = current
                current = 0
        
        return current if current > ans else ans
        

        