class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        pointerS = 0
        answer = ''
        
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        for i in range(len(t)):
            if t[i] == s[pointerS]:
                pointerS += 1

            if pointerS == len(s):
                return True
        return False    
        
        
        
                
