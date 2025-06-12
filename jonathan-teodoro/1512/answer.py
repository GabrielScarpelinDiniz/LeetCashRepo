class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = [0] * 101  
        for num in nums:
            freq[num] += 1

        good_pairs = 0
        for f in freq:
            if f >= 2:
                good_pairs += f * (f - 1) // 2

        return good_pairs