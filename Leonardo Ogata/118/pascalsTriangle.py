class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        piramid = [[1], [1, 1]]

        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        x = 2

        while x < numRows:
            newRoll = [0] * (x + 1)
            newRoll[0] = 1
            newRoll[-1] = 1

            for i in range(1, len(newRoll) - 1):
                newRoll[i] = piramid[x-1][i-1] + piramid[x-1][i]
            piramid.append(newRoll)

            x += 1
        
        return piramid
    