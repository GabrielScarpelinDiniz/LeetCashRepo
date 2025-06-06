class Solution(object):
    def heightChecker(self, heights):
        nova_lista = sorted(heights)
        resposta = 0
        for i in range(len(heights)):
            if heights[i] != nova_lista[i]:
                resposta+=1
        return resposta
        