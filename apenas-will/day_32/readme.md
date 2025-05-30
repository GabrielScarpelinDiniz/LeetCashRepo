## Exercício: 226. Invert Binary Tree
**Objetivo**: Dada uma árvore binária, inverta-a (os dós da esquerda vão para a direita e vice-versa);

## Descrição geral da estratégia
Para resolver, usei uma abordagem recursiva que vai invertendo os nós da sub-árvore da esquerda e da direita, _in-place_ e de baixo para cima.

## Análise de complexidade
Para uma árvore com $n$ nós, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(\log(n))$ (para árvores balanceadas) 