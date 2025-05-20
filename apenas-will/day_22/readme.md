## Exercício: 412. Fizz Buzz
**Objetivo**: Dada a raiz de uma árvore binária, determine sua altura máxima (maior quantidade de nodes entre a raiz e uma folha);

## Descrição geral da estratégia
Para resolver, implementei um DFS recursivo, incrementando 1 ao valor de um contador e retornando a altura máxima encontrada entre as alturas da subárvore da direita e esquerda.

## Análise de complexidade
Para uma árvore com $n$ nodes, tem-se:
- **Time complexity**: $O(\log(n))$
- **Space complexity**: $O(1)$ 