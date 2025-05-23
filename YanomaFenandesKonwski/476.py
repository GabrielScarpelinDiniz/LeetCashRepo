class Solution(object):
    def findComplement(self, num):
        bin_str = ""
        n = num
        while n > 0:
            resto = n % 2
            bin_str = str(resto) + bin_str
            n = n // 2

        inverted_str = ""
        for caractere in bin_str:
            if caractere == '1':
                inverted_str += '0'
            else:
                inverted_str += '1'

        resultado = 0
        expoente = 0
        for i in range(len(inverted_str) - 1, -1, -1):
            bit = int(inverted_str[i])
            resultado += bit * (2 ** expoente)
            expoente += 1
        return resultado