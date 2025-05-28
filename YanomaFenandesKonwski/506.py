class Solution(object):
    def findRelativeRanks(self, score):
        lista = sorted(score, reverse = True)
        respostas = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        resposta = []
        rep = 0
        for i in range(len(lista)):
            rep = lista.index(score[i])
            rep+=1
            if rep == 1:
                resposta.append(str(respostas[0]))
            elif rep == 2:
                resposta.append(str(respostas[1]))
            elif rep == 3:
                resposta.append(str(respostas[2]))
            else:
                resposta.append(str(rep))
        return resposta


