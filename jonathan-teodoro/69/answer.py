class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return 0 
