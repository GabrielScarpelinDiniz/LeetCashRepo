# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2037, que pede para calcular o número mínimo de movimentos para sentar cada estudante em uma cadeira, onde cada movimento é andar uma unidade. Para isso, segui os seguintes passos:

1. Ordenei as listas `seats` e `students`.

2. Criei uma variável `movimentos` para contar o total de movimentos necessários.

3. Usei um for para passar por cada cadeira e estudante:

    3.1. Para cada par, somei a diferença absoluta entre a posição da cadeira e do estudante em `movimentos`.

4. No final, retornei `movimentos` como resposta.

E pronto! Mais um exercício resolvido!!!