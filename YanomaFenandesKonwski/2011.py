class Solution(object):
    def finalValueAfterOperations(self, operations):
        resposta = 0
        for i in range(len(operations)):
            if operations[i]=="++X" or operations[i]=="X++":
                resposta+=1
            else:
                resposta-=1
        return resposta
        