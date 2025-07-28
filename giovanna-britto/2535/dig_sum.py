class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        numsSoma = sum(nums)
        total = 0
        for n in nums:
            for n2 in str(n):
                total += int(n2)

        return abs(numsSoma - total)