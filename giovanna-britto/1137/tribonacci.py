class Solution:
    def __init__(self):
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            self.memo[1] = 1
        elif n == 0:
            self.memo[0] = 0
        elif n == 2:
            self.memo[2] = 1
        else:
            self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
        return self.memo[n]