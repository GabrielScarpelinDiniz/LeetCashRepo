class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        contador = 0
        for letra1 in jewels:
            for letra2 in stones:
                if letra1 == letra2:
                    contador+=1
        return contador

        