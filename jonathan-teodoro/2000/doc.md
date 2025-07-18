class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        lista = []
        index = 0
        find = False
        for i in range(len(word)):
            lista.append(word[i])
            if word[i] == ch and not find:
                index = i
                find = True
        l = 0
        r = index

        while (l <= r):
            lista[l], lista[r] = lista[r], lista[l]
            l += 1
            r -= 1

        word = ""
        for i in lista:
            word += i
        return word               

COMPLEXIDADE PÉSSIMA. MUITO MAL FEITO, MAS ANTES MALFEITO QUE NÃO FEITO. O código resolve o problema de inverter o prefixo da string word até o primeiro caractere ch, mas faz isso de forma ineficiente: cria uma lista extra com todos os caracteres da string, faz a inversão com dois ponteiros mesmo podendo usar slicing, e depois reconstrói a string manualmente caractere por caractere. Embora funcione corretamente, há redundância e custo desnecessário de tempo e memória.