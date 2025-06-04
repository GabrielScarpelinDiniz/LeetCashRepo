class Solution:
    def balancedStringSplit(self, s: str) -> int:
        resultado = 0 
        balanceamento = 0 

        for i in s:
            if i == 'R':
                balanceamento += 1
            else: 
                balanceamento -= 1

            if balanceamento == 0:
                resultado += 1
        return resultado