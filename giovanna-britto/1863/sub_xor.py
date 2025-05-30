from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for r in range(n + 1):  # r é o tamanho do subconjunto
            for subset in combinations(nums, r):
                xor_sum = 0
                for num in subset:
                    xor_sum ^= num
                total += xor_sum

        return total
