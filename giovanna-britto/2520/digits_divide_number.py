class Solution:
    def countDigits(self, num: int) -> int:
        nS = str(num)
        arr = list(nS)
        cont = 0
        
        for i in range(len(arr)):
            if(num % int(arr[i]) == 0):
                cont += 1
        
        return cont