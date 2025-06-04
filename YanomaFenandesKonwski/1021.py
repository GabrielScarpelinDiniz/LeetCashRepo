class Solution(object):
    def removeOuterParentheses(self, s):
        resultado = []
        profundidade = 0

        for caractere in s:
            if caractere == '(':
                if profundidade > 0:
                    resultado.append('(')
                profundidade += 1
            elif caractere == ')':
                profundidade -= 1
                if profundidade > 0:
                    resultado.append(')')
        
        return ''.join(resultado)