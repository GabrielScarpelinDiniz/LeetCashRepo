# Mais um dia de LeetCash

Hoje resolvi o exercício 2635, que pede para implementar uma função `map` em JavaScript, igual ao método `.map()` dos arrays. Resolvi assim:

1. Criei a função `map` que recebe um array `arr` e uma função `fn`.
2. Criei um array vazio `newArr` para guardar os resultados.
3. Usei um for para passar por cada elemento do array original.
    3.1. Para cada elemento, chamei `fn` passando o valor e o índice, e coloquei o resultado na posição correspondente de `newArr`.
4. No final, retornei `newArr` com todos os valores transformados.

E pronto! Mais um exercício resolvido!!!