# Mais um dia de LeetCash

Hoje eu resolvi o exercício 1379, que consiste em encontrar um nó correspondente de uma árvore binária em um clone dessa árvore, no qual, dado uma árvore `original`, uma árvore `cloned` (que é uma cópia exata da `original`), e um nó `target` presente na árvore `original`, o desafio era encontrar esse mesmo nó na árvore `cloned` e retornar a referência dele. Para isso eu segui os seguintes passos:

1. Criei uma função recursiva que percorre simultaneamente as duas árvores (`original` e `cloned`).
2. A cada nó, eu verifico:

   2.1. Se o nó atual da `original` é igual ao `target`, então retorno  o nó da árvore `cloned` que está na mesma posição.

3. Se não for:

   3.1. Tento buscar primeiro no filho da esquerda.

   3.2. Se não encontrar, busco no filho da direita.

4. Quando encontrar, retorno o nó da árvore `cloned`.

E é isso! Mais um exercício resolvido!!