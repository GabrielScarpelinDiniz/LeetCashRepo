class Solution(object):
    def numOfStrings(self, patterns, word):
        resposta = 0
        for i in range(len(patterns)):
            if patterns[i] in word:
                resposta+=1
        return resposta
        