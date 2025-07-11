class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        elif t == "":
            return False

        first = 0
        second = 0

        while second < len(t):
            if s[first] == t[second]:
                first += 1
                second += 1
            else:
                second += 1

            if first == len(s):
                return True

        return False 
        