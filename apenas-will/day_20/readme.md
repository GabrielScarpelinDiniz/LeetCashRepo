## Exercício: 145. Binary Tree Postorder Traversal
**Objetivo**: Dada um node que é a raiz de uma árvore binária, faça uma passagem transversal em pós ordem;

## Descrição geral da estratégia
Para resolver, fiz o transversal, adicionando o nó da esquerda em uma lista de soluções, depois o nó da direita e, por último, a raiz de forma recursiva.

## Análise de complexidade
Para uma árvore com $n$ nodes, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$ (para gerar o output, $O(1)$ espaço auxiliar)