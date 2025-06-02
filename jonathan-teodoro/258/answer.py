class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def recursion(num):
            answer = []
            for i in str(num):
                answer.append(int(i))
            sum = 0
            for j in answer:
                sum += j

            if len(str(sum)) > 1:
                return recursion(sum)
            else:
                print(sum)
                return sum


        value = recursion(num)
        return value