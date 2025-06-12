class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newS = [''] * len(s)
        for i in range(len(s)):
            newS[indices[i]] = s[i]
    
        return ''.join(i for i in newS)
