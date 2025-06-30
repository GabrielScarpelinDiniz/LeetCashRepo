class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dick = Counter(s)

        for i in dick:
            if dick[i] == 1:
                return s.index(i) 
        return -1