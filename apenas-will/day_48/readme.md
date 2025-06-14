## Exercício: 39. Combination Sum
**Objetivo**: Dado um array de inteiros e um `target`, retorne todas as combinações de elementos do array que a soma é igual ao `target`;

## Descrição geral da estratégia
Para resolver implementei um algoritmo de backtracking que gera as combinações, conferindo se a soma delas é igual ao `target`. Caso a soma satisfaça a condição, a combinação é adicionada à solução, sendo descartada caso contrário.

## Análise de complexidade
Para um array com $n$ candidatos, tem-se:
- **Time complexity**: $O(2^n)$
- **Space complexity**: $O(2^n)$ ( $\Theta(1)$ se considerar só espaço auxiliar) 