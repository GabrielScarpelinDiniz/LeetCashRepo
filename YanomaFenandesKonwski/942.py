class Solution(object):
    def diStringMatch(self, s):
        menor, maior = 0, len(s)
        resultado = []
        for char in s:
            if char == 'I':
                resultado.append(menor)
                menor += 1
            else: 
                resultado.append(maior)
                maior -= 1
        resultado.append(menor)
        return resultado