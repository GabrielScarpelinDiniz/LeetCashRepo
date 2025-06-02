class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            inicio = max(0, i - nums[i])
            sub_soma = sum(nums[inicio:i+1])
            total += sub_soma
        return total
