class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0

        if(x > 0):
            while(x > 0):
                reverse = (reverse * 10) + (x % 10)
                x = x/10
        else:
            x = x * -1
            while(x > 0):
                reverse = (reverse * 10) + (x % 10)
                x = x/10
            reverse = reverse * -1

        if (abs(reverse) > 2147483647):
            return 0
        return reverse