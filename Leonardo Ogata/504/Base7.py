class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = False

        if num < 0:
            neg = True
            num *= -1
            
        string = ""

        while num > 0:
            string += str(num % 7)
            num = num // 7

        reverse = string[::-1]
        
        return reverse if neg == False else (str(int(reverse) * -1))
        