# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2859, que pede para somar os valores de um array cujos índices têm exatamente `k` bits 1 na representação binária. Para isso eu segui os seguintes passos:

1. Criei uma variável `total` para acumular a soma dos valores.

2. Usei `enumerate` para passar por cada valor e seu índice em `nums`.

3. Para cada índice, contei quantos bits 1 ele tem usando `bin(i).count('1')`.

4. Se o número de bits 1 for igual a `k`, somei o valor correspondente em `total`.

5. No final, retornei `total` com a soma dos valores dos índices que atendem a condição.

E pronto! Mais um exercício resolvido!!