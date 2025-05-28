class Solution:
    def numberOfSteps(self, num: int) -> int:
        cont = 0
        while (num != 0):
            if (num % 2 == 0):
                num = num/2
                cont += 1
            else:
                num -= 1
                cont += 1
        return cont
