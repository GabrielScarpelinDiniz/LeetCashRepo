# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2373, que pede para construir uma nova matriz onde cada elemento é o maior valor de uma submatriz 3x3 da matriz original. Para isso eu segui os seguintes passos:

1. Descobri o tamanho da matriz `grid` e criei uma lista vazia `maxLocal` para guardar o resultado.

2. Usei dois fors para percorrer todas as posições possíveis do canto superior esquerdo de cada submatriz 3x3.

3. Para cada posição, calculei o maior valor entre os 9 elementos da submatriz 3x3 usando a função `max`.

4. Adicionei esse valor em uma linha temporária `row`.

5. Depois de preencher a linha, adicionei ela em `maxLocal`.

6. No final, retornei `maxLocal` com todos os maiores valores locais.

E pronto! Mais um exercício resolvido!!