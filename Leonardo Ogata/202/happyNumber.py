class Solution:
    def isHappy(self, n: int) -> bool:

        def checkHappy(n, limit):
            if limit > 20:
                return False
            
            if n == 1:
                return True

            ans = 0
        
            while n > 0:
                ans += (n % 10)**2
                n = n // 10
            
            return True if ans == 1 else checkHappy(ans, limit + 1)

        if n == 1:
            return True
        else:
            return checkHappy(n, 0)     