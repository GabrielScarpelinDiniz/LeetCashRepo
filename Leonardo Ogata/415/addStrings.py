class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        size = max(len(num1), len(num2))

        arrNum1 = []
        arrNum2 =[]

        for i in range(size -1, -1, -1):
            if i < len(num1):
                arrNum1.append(num1[i])
            if i < len(num2):
                arrNum2.append(num2[i])
        
        if len(arrNum1) < len(arrNum2):
            smallest = arrNum1
            biggest = arrNum2
        else:
            smallest = arrNum2
            biggest = arrNum1
        

        while len(smallest) < len(biggest):
            smallest.append("0")

        carry = 0   
        ans = ""

        for i in range(len(arrNum1)):
            summer = dic[arrNum1[i]] + dic[arrNum2[i]] + carry

            if summer < 10:
                ans += str(summer)
                carry = 0
            else: 
                ans += str(summer % 10)
                carry = summer // 10
        
        if carry != 0:
            ans += str(carry)
        
        return ans[::-1]
        

