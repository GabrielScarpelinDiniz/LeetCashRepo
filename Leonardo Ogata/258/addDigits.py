class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if num <= 9:
            return num
        else:
            return 1 + (num - 1) % 9