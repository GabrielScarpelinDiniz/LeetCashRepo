class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        summer = 0

        for i in stones:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in jewels:
            if i in dic:
                summer += dic[i]
        
        return summer