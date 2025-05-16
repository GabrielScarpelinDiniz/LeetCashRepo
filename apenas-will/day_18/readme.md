## Exercício: 144. Binary Tree Preorder Traversal
**Objetivo**: Dada um node que é a raiz de uma árvore binária, faça uma passagem transversal em ordem;

## Descrição geral da estratégia
Para resolver, fiz o transversal, adicionando a raiz em uma lista de soluções, depois o nó da esquerda e, por último, o nó da direita de forma recursiva.

## Análise de complexidade
Para uma árvore com $n$ nodes, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$ (para gerar o output, $O(1)$ espaço auxiliar)