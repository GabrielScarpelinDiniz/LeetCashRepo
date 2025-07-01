class Solution(object):
    def isSameAfterReversals(self, num):
        def reverso(n):
            resultado = 0
            while n > 0:
                resultado = resultado * 10 + (n % 10)
                n //= 10
            return resultado

        def double_reverso(n, vezes):
            if vezes == 0:
                return n
            return double_reverso(reverso(n), vezes - 1)

        return num == double_reverso(num, 2)
                

                
        