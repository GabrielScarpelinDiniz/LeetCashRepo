class Solution(object):
    def findComplement(self, num):
        bin_str = ""
        n = num
        while n > 0:
            resto = n % 2
            bin_str = str(resto) + bin_str
            n = n // 2

        inverte = ""
        for caractere in bin_str:
            if caractere == '1':
                inverte += '0'
            else:
                inverte += '1'

        resultado = 0
        expoente = 0
        for i in range(len(inverte) - 1, -1, -1):
            bit = int(inverte[i])
            resultado += bit * (2 ** expoente)
            expoente += 1
        return resultado