class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        resposta = ""
        cont = 0

        for i in s:
            if i == '(':
                if cont >= 1:
                    resposta += i
                cont += 1
            else:
                cont -= 1
                if cont >= 1:
                    resposta += i
        return resposta