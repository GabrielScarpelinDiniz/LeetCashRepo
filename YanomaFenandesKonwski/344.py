class Solution(object):
    def reverseString(self, s):
        esquerda, direita = 0, len(s) -1
        while esquerda<direita:
            s[esquerda], s[direita] = s[direita], s[esquerda]
            direita-=1
            esquerda+=1
        return s