## Exercício: 77. Combinations
**Objetivo**: Dado um valor $n$ e $k$, retorne todas as combinações de $k$ elementos que estão no conjunto de 1 à $n$ incluso;

## Descrição geral da estratégia
Para resolver implementei um algoritmo de backtracking que gera cada uma das combinações, usando como critério de parada o tamanho da solução que está sendo construída.

## Análise de complexidade
Para os valores $n$ e $k$, tem-se:
- **Time complexity**: $O(\frac{n!}{(n-k)! \cdot k!})$
- **Space complexity**: $O(\frac{n!}{(n-k)! \cdot k!})$ 