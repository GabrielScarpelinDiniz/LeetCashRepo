class Solution:
    def fib(self, n: int) -> int:
        self.memo = {}

        if n in self.memo:
            return self.memo[n]
        if n == 1:
            self.memo[1] = 1
        elif n == 0:
            self.memo[0] = 0
        else:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.memo[n]