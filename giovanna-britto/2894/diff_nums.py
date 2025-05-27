class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        numDiv = []
        numNdiv = []

        for i in range(1, n+1):
            if (i % m == 0):
                numDiv.append(i)
            else:
                numNdiv.append(i)
        
        num1 = sum(numNdiv)
        num2 = sum(numDiv)

        return int(num1 - num2)