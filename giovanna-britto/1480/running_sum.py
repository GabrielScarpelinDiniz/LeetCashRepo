class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        memo = []
        num = 0
        for i in range(0, (len(nums))):
            num += nums[i]
            memo.append(num)

        return memo