class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        summer = 0

        for i in range(1, int(num**0.5) + 1):
            if not num % i:
                summer += i + num//i
        
        return summer - num == num
