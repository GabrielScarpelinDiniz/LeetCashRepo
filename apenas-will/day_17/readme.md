## Exercício: 98. Validate Binary Search Tree
**Objetivo**: Dada um node que é a raiz de uma árvore binária, determine se é uma árvore binária de busca;

## Descrição geral da estratégia
Para resolver gerei um array que continha a ordenação em ordem dessa árvore. Se ela for uma árvore binária de busca, esse array estará ordenado de maneira crescente. Sendo assim, basta conferir se todo elemento de índice $i$ é menor que o elemento em $i + 1$, retornando `false` caso essa condição não seja atendida e `true` caso contrário.

## Análise de complexidade
Para uma árvore com $n$ nodes, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$