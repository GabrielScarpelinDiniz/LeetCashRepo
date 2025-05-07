## Exercício: 217. Contains Duplicate
**Objetivo**: Dado um array de inteiros, determine se há ou não valores duplicados.

## Descrição geral da estratégia
Para resolver, gerei um set contendo todos os elementos, caso houvesse algum elemento repetido, retornava `true`, retornando `false` caso contrário.

## Análise de complexidade
Para um array com $n$ elementos, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$
