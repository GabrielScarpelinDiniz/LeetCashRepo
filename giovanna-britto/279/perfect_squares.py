class Solution:
    def numSquares(self, n: int) -> int:
        memo = [-1]*(n+1)

        if n == 0:
            return 0
        if n < 0:
            return float('inf')
        if memo[n] != -1: 
            return memo[n]
        
        mini = n
        i = 1
        while i * i  <= n:
            mini = min(mini, self.numSquares(n-(i*i)))
            i+=1
        memo[n] = mini+1
        return memo[n]