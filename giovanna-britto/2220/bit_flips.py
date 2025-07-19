class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        resultado = start ^ goal
        resposta = 0 

        while resultado > 0:
            resposta += resultado & 1
            resultado >>= 1

        return resposta