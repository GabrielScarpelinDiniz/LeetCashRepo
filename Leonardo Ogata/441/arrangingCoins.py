class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while n > 0:
            n -= i
            i +=1

        return i - 2 if n < 0 else i - 1
        