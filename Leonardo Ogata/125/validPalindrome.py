class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([char for char in s if char.isalnum()])
        s = s.lower()

        print(s)

        inverted = s[::-1]
        
        print(inverted)

        return s == inverted