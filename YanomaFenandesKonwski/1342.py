class Solution(object):
    def numberOfSteps(self, num):
        resposta = 0
        while num>=1:
            porenquanto = num%2
            if porenquanto ==1:
                num -=1
                resposta+=1
            else:
                num//=2
                resposta+=1
        return resposta
        