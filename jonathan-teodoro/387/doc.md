class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicionario = {}
        for i in s:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1
        
        for i in range(len(s)):
            if dicionario[s[i]] and dicionario[s[i]] == 1:
                return i
        
        return -1

Bom exercício de hashmap pra treinar. Bem facinho. Percorro a string e adiciono os valores em um hashmap junto com suas frequencias. Feito isso, percorro a string em ordem. O caracter da string é a chave do dicionario, entao faco uma busca no dicionario que é o(1) para cada item da string, o primeiro que for 1 eu retorno, se nenhum for eu retorno -1. Trivial.