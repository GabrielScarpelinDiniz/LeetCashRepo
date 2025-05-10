n = 11
auxiliar = 0
dicionario = {0:0, 1:0}
while n>=1:
    if n%2 == 1:
        dicionario[1] +=1
    else:
        dicionario[0] += 1
    n = int(n/2)

print (dicionario[1])


