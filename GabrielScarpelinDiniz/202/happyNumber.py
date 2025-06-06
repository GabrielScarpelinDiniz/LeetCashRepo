class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def checkIfIsHappyRecursive(num, setVerifyLoop):
            numCurrent = num
            digits = []
            while numCurrent != 0:
                digits.append(numCurrent % 10)
                numCurrent = numCurrent // 10

            digits = [d ** 2 for d in digits]
            newNum = sum(digits)
            if newNum == 1:
                return True

            if newNum in setVerifyLoop:
                return False

            setVerifyLoop.add(newNum)
            return checkIfIsHappyRecursive(newNum, setVerifyLoop)

        return checkIfIsHappyRecursive(n, set())
