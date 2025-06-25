class Solution(object):
    def mostWordsFound(self, sentences):
        resultado = 0
        auxiliar = 1
        for i in range(len(sentences)):
            for letra in sentences[i]:
                if letra == " ":
                    auxiliar+=1
            if auxiliar>resultado:
                resultado = auxiliar
            auxiliar=1
        return resultado
        