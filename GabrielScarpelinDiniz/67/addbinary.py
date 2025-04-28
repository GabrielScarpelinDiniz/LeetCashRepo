class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxLen = max(len(a), len(b))
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        elif len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b

        needToAdd = 0
        binaryStr = ""
        for idx in range(maxLen - 1, -1, -1):
            firstBinary = int(a[idx])
            secondBinary = int(b[idx])
            sum = firstBinary + secondBinary + needToAdd
            print(sum)
            if sum > 1:
                binNum = sum - 2
                binaryStr = str(binNum) + binaryStr
                needToAdd = sum // 2
            else:
                needToAdd = 0
                binaryStr = str(sum) + binaryStr

        if needToAdd == 1:
            binaryStr = "1" + binaryStr
        if needToAdd == 2:
            binaryStr = "10" + binaryStr
        return binaryStr
