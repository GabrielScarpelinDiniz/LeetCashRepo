class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cont = 0
        for i in stones:
            if i in jewels:
                cont += 1
        return cont

        