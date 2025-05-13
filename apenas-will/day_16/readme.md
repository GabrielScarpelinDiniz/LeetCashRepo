## Exercício: 238. Product of Array Except Self
**Objetivo**: Dada uma array de inteiros, retorne um array que, em um determinado índice, tenha o valor do produto de todos os elementos exceto aquele que estava nesse índice no array inicial. e.g. 
> - Input: [1, 2, 3];
> - Output: [6, 3, 2];
> - Explicação: No índice 0, temos 6, que é igual ao produto de todos os elementos do array, exceto o 1, que estava nesse índice no input. De maneira semelhante, 3 = 3 * 1 (todo os elementos exceto o dois) e 2 = 1 * 2 (todos os elementos exceto o 3).

> [!WARNING]
> Não é permitido o uso da operação de divisão no desafio;

## Descrição geral da estratégia
Para resolver criei dois arrays, um contendo o produto de todos os elementos anteriores a um determinado elemento $i$ e uma com o produto de todos os elementos posteriores a esse elemento $i$. Por fim, bastou multiplicar os elementos correspondentes, gerando o resultado;

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$