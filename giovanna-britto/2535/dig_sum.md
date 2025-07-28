# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2535, que pede para calcular a diferença entre a soma dos elementos de um array e a soma dos dígitos desses elementos. Resolvi assim:

1. Calculei a soma dos elementos do array `nums` e salvei em `numsSoma`.
2. Criei uma variável `total` para somar todos os dígitos dos números.
3. Usei um for para passar por cada número do array.
    3.1. Para cada número, transformei em string e somei cada dígito em `total`.
4. No final, retornei o valor absoluto da diferença entre `numsSoma` e `total`.

E pronto! Mais um exercício resolvido!!!