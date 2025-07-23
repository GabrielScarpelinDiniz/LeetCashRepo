class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ans = ""

        for i in s:
            ans += i
            if len(s) % len(ans) == 0 and ans * (len(s) // len(ans)) == s and len(s) // len(ans) != 1:
                return True
        
        return False