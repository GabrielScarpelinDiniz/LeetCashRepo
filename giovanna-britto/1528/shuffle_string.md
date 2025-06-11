# Mais um dia de LeetCash

Hoje resolvi o exercício 1528, que pede para embaralhar uma string de acordo com um array de índices. Para cada posição do array, preciso colocar o caractere da string original na posição indicada pelo índice. Para isso segui os seguintes passos:

1. Criei uma lista `newS` do mesmo tamanho da string `s`, só com strings vazias.
2. Usei um for para passar por cada caractere da string `s`:

    2.1. Para cada posição `i`, coloquei o caractere `si]` na posição `indicesi]` da lista `newS`.

3. No final, juntei todos os caracteres de `newS` em uma string só e retornei como resposta.

E pronto! Mais um exercício resolvido!