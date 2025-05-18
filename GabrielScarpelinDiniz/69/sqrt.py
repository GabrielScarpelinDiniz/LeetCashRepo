class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i * i < x:
            i += 1
        if i * i > x:
            return i - 1
        else:
            return i
