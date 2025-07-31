
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0

        for i, valor in enumerate(nums):
            if(bin(i).count('1') == k):
                total += valor
        return total