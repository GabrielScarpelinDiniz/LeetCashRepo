class Solution(object):
    def hammingWeight(self, n):
        dicionario = {0:0, 1:0}
        while n>=1:
            if n%2 == 1:
                dicionario[1] +=1
            else:
                dicionario[0] += 1
            n = int(n/2)
        return dicionario[1]