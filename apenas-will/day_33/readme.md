## Exercício: 543. Diameter of Binary Tree
**Objetivo**: Dada uma árvore binária, indique o seu diâmetro (maior distância entre dois nós);

## Descrição geral da estratégia
Para resolver, usei uma abordagem recursiva na qual calcula-se a altura da sub-árvore da esquerda e da direita, somando esses valores e armazenando o maior deles em uma variável global.

## Análise de complexidade
Para uma árvore com $n$ nós, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$ , ( $O(\log(n))$ para árvores balanceadas) 