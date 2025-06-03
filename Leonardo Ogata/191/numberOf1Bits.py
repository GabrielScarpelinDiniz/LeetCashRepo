class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_value = int(bin(n)[2:])

        counter = 0

        while binary_value > 0:
            if binary_value % 10 == 1:
                counter += 1
            binary_value /= 10
        
        return counter


    