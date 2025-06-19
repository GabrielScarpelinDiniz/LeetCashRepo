class Solution(object):
    def balancedStringSplit(self, s):
        L_count=0
        R_count=0
        resposta=0
        for letra in s:
            if letra=="R":
                R_count+=1
            else:
                L_count+=1
            if R_count==L_count:
                resposta+=1
                R_count=0
                L_count=0
        return resposta


        