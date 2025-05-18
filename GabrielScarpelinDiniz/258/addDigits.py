class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        num_str = str(num)
        result = 0
        while result >= 10 or result <= 0:
            result = 0
            split_str = list(num_str)
            for i in split_str:
                result += int(i)

            num_str = str(result)

        return result
