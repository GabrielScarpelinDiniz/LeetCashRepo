class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for num in nums:
            resto = num % 3
            if resto == 1:
                ops += 1  
            elif resto == 2:
                ops += 1  
        return ops
