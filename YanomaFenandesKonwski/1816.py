class Solution(object):
    def truncateSentence(self, s, k):
        palavra=""
        lista=[]
        resposta=""
        for letra in s:
            if letra == " ":
                lista.append(palavra)
                palavra=""
            palavra+=letra
        lista.append(palavra)
        print(lista)
        for i in range(k):
            resposta+=lista[i]
        return resposta


        