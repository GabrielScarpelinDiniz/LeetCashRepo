class Solution(object):
    def reversePrefix(self, word, ch):
        fim = 0
        while fim<(len(word)-1) and word[fim]!=ch:
            fim+=1
        if word[fim] != ch:
            return word
        else:
            prefixo = word[:fim+1][::-1]
            resto = word[fim+1:]
        return prefixo+resto
            

        