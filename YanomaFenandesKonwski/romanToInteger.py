class Solution(object):
    def romanToInt(self, s):
        soma = 0
        antigo = 0
        for indice in range(len(s)):
            caractere = s[indice]
            if caractere == "I":
                numero = 1
            elif caractere == "V":
                numero = 5
            elif caractere == "X":
                numero = 10
            elif caractere == "L":
                numero = 50
            elif caractere == "C":
                numero = 100
            elif caractere == "D":
                numero = 500
            elif caractere == "M":
                numero = 1000
            else:
                raise KeyError("Caractere inválido")

            if numero>antigo and antigo !=0:
                soma+=numero
                soma-=antigo*2
            else:
                soma+=numero
            antigo=numero
        return soma
        