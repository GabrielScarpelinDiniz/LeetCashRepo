lista = s.split()
resposta = []

for palavra in lista:
    palavra_invertida = palavra[::-1]
    resposta.append(palavra_invertida)

resultado = ' '.join(resposta)
