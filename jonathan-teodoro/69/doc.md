class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return 0 


69!!!!!!!!
Exercicio mais aguardado!! Binary searchzinha de lei!!! Bem simplinha, tem dois casos aqui - se cravar o valor ou se um é menor e proximo é maior. Fiz dinâmica pq prefiro. Binary search recursiva ta com nada. Mole mole. Beijos do gordo, até amn!