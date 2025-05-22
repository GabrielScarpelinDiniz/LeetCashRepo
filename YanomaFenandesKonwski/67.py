def addBinary(a, b):
    numeroa = int(a)
    numerob = int(b)
    lista = []
    listab = []
    binario = []
    soma = 0
    numero = 0

    def converte(numero, lista):
        while numero > 0:
            lista.append(numero % 10)
            numero //= 10

    converte(numeroa, lista)
    converte(numerob, listab)

    for i in range(len(lista)):
        soma += lista[i] * (2 ** i)
    for i in range(len(listab)):
        soma += listab[i] * (2 ** i)

    while soma > 0:
        binario.append(soma % 2)
        soma //= 2
    

    for i in range(len(binario)):
        numero+= binario[i] * (10**i)

    return numero

print(addBinary("11", "1"))
        


