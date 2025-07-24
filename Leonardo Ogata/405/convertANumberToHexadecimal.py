class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return  "0"

        if num < 0:
            num = (1 << 32) + num
    
        return convertToHex(num)

def convertToHex(num: int) -> str:
        dic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        hexa = "" 
        
        while num > 0:
            temp = num % 16

            if temp < 10:
                hexa += str(temp)
            else:
                hexa += dic[temp]
            
            num = num // 16

        return hexa[::-1]
                 
        