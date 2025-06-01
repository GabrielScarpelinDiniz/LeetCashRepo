# Mais um dia de LeetCash

Hoje eu resolvi o exercício 1281, no qual dado uma entrada n, eu deveria retornar a diferença entre o produtos dos digitos de n e a soma dos digitos de n. Para isso eu segui os seguintes passos:

1. Crio um variável `nS` que recebe n convertida em String
2. Eu divido a string em um array
3. Defino uma variável `sum` para armazenar a soma e uma `mult` para retornar a multiplicação
4. Faço um for para iterar sobre esse array
    4.1. Adiciono `int(nS[i])` na sum
    4.2. Multiplico `int(nS[i])` em mult
5. Retorno a diferença entre mult e sum

E pronto! Mais um resolvido!!!