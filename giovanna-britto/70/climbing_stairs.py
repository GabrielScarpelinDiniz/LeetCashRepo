class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
           return 1
        if n == 2:
            return 2

        possibilidades = [0] * n
        possibilidades[0] = 1
        possibilidades[1] = 2

        for i in range(2, n):
            possibilidades[i] = possibilidades[i-1] + possibilidades[i-2]

        return possibilidades[n-1]