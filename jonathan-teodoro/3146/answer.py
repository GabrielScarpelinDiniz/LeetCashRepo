class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        map_s = {}
        for i in range(len(s)):
            map_s[s[i]] = i
        
        total = 0
        for i in range(len(t)):
            char = t[i]
            pos_in_s = map_s[char]
            total += abs(i - pos_in_s)
        
        return total
