class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nS = str(n)
        nS.split()
        sum = 0
        mult = 1
        for i in range(len(nS)):
            sum += int(nS[i])
            mult *= int(nS[i])

        return mult - sum
