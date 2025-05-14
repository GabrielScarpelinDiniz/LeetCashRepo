class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        maior_valor = max(nums)
        points = [0] * (maior_valor + 1)

        for i in nums:
            points[i] += i
        
        dp = [0] * (maior_valor+1)
        dp[0] = 0
        dp[1]= points[1]

        for i in range(2, maior_valor + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

        return dp[maior_valor]