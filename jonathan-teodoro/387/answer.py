class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicionario = {}
        for i in s:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1
        
        for i in range(len(s)):
            if dicionario[s[i]] and dicionario[s[i]] == 1:
                return i
        
        return -1

        