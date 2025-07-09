class Solution(object):
    def countAsterisks(self, s):
        auxiliar = 0
        resp=0
        for caracter in s:
            if caracter=="|" and auxiliar==0:
                auxiliar+=1
            elif caracter=="|" and auxiliar==1:
                auxiliar-=1
            elif caracter=="*" and auxiliar==0:
                resp+=1
        return resp


        