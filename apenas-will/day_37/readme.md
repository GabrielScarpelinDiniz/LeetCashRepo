## Exercício: 46. Permutations
**Objetivo**: Dada um array de inteiros, retorne uma lista com todas as permutações formadas com esses inteiros;

Exemplo:
> **Input:** [1, 2, 3]
>
> **Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


## Descrição geral da estratégia
Para resolver, implementei um algoritmo de backtracking que gera todas as permutações.

## Análise de complexidade
Para um array com $n$ elementos, tem-se:
- **Time complexity**: $O(n!)$ ( $\Theta(n \cdot n!)$ )
- **Space complexity**: $O(n!)$ 