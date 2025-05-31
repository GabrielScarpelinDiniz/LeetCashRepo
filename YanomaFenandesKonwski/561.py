class Solution(object):
    def arrayPairSum(self, nums):
        lista_ordenada = sorted(nums)
        pares = 0
        resultado = 0
        while pares<len(lista_ordenada):
            resultado += min(lista_ordenada[pares], lista_ordenada[pares+1])
            pares+=2
        return resultado

        