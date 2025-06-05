class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = None
        counter = -1

        while power < n:
            counter += 1 
            power = 2 ** counter
        
        return True if power == n else False

            