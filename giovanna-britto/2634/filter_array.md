# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2634, que pede para implementar uma função `filter` em JavaScript, igual ao método `.filter()`. Para isso segui os seguintes passos:

1. Criei a função `filter` que recebe um array `arr` e uma função `fn`.
2. Criei um array vazio `filtro` para guardar os valores filtrados.
3. Usei um for para passar por cada elemento do array original.
    3.1. Para cada elemento, chamei `fn` passando o valor e o índice.
    3.2. Se a função retornar `true`, adiciono o elemento em `filtro`.
4. No final, retornei `filtro` com todos os valores que passaram no filtro.

E pronto! Mais um exercício resolvido!!!