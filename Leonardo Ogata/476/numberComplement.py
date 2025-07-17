class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        ans = ""
        
        for i in range(2, len(num)):
            if num[i] == "0":
                ans += "1"
            else:
                ans += "0"
        
        return int(ans, 2)

        