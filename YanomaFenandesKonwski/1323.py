class Solution(object):
    def maximum69Number (self, num):
        lista = []
        while num > 0:
            lista.append(num % 10)
            num //= 10
        lista.reverse()
        for i in range(len(lista)):
            if lista[i] == 6:
                lista[i] = 9
                break
        resposta = 0
        rodadas = len(lista) - 1
        for digito in lista:
            resposta += digito * (10 ** rodadas)
            rodadas -= 1
        return resposta


        