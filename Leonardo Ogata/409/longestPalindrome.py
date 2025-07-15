class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = 1 
            else:
                dic[i] += 1 

        summer = 0
        isEven = False

        for i in dic:
            if dic[i] % 2 == 0:
                summer += dic[i]
            else:
                isEven = True
                summer += dic[i] - 1

        return summer + 1 if isEven else summer