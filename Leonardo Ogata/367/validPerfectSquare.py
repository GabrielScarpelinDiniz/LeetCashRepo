class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 0
        high = num
        mid = 0
        
        while low <= high:

            mid = (low + high) // 2

            if mid * mid == num:
                return True
            
            elif mid * mid > num:
                high = mid - 1

            elif mid * mid < num:
                low = mid + 1
        
        return False