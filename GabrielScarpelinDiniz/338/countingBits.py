class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n + 1):
            _0, binary = bin(i).split("b")
            currentNum = int(binary)
            digits = []

            while currentNum > 0:
                digits.append(currentNum % 10)
                currentNum = currentNum // 10
            result.append(sum(digits))

        return result
