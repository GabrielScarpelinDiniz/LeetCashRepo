class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stack = []        

        if x<0:
            return False

        for i in str(x):
            stack.append(i)

        for i in stack:
            poped = stack.pop()
            if i != poped:
                return False

        return True   
        

        
            