class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            answer = "-"
        else:
            answer = ""

        for i in str(x)[::-1]:
            if i != "-":
                answer += i
        print(answer)
        
        if int(answer).bit_length() >= 32:
            return 0
        return int(answer)
        