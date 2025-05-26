class Solution(object):

    def hammingDistance(self, x, y):
        x = bin(x)
        y = bin(y)
        tamanho = max(len(x), len(y))
        listax = [int(bit) for bit in x[2:].zfill(tamanho)]  
        listay = [int(bit) for bit in y[2:].zfill(tamanho)]
        resposta = 0
        for i in range(len(listay)):
            if listax[i]!=listay[i]:
                resposta+=1
        return resposta

        


        