class Solution(object):
    def romanToInt(self, s):
        romanos = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        ultimo = 0

        for i in reversed(s):
            valor = romanos[i]
            if valor < ultimo:
                total -= valor  
            else:
                total += valor 
            ultimo = valor

        return total

            