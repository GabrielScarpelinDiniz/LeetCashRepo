class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""

        for i in address:
            if i == ".":
                ans += "[.]"
            else:
                ans += i
        
        return ans
        