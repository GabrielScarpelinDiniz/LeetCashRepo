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