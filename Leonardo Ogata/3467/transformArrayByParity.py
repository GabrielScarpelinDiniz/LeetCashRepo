class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        zeroes = 0
        ones = 0

        for i in nums:
            if i % 2 == 0:
                zeroes += 1
            else:
                ones += 1
        
        for i in range(zeroes):
            ans.append(0)

        for i in range(ones):
            ans.append(1)

        return ans