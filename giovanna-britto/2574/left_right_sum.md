# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2574, que pede para calcular para cada posição de um array a diferença absoluta entre a soma dos elementos à esquerda e à direita. Para isso eu segui os seguintes passos:

1. Criei uma lista `answer` para guardar as respostas

2. Calculei a soma total do array `nums` e salvei em `somaTotal`.

3. Criei uma variável `somaEsq` para acumular a soma da esquerda.

4. Usei um for para passar por cada elemento do array:

    4.1. Calculei a soma da direita como `somaTotal - somaEsq - nums[i]`.

    4.2. Coloquei em `answer[i]` o valor absoluto da diferença entre a soma da esquerda e da direita.

    4.3. Somei o valor atual em `somaEsq` para atualizar a soma da esquerda.

5. No final, retornei `answer` com todas as diferenças calculadas.

E pronto! Mais um exercício resolvido!!