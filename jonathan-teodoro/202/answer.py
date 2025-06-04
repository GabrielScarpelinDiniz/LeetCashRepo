class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            sum = 0

            for i in str(n):
                square = int(i)*int(i)
                sum += square
            n = sum
        
        return True