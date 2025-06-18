## Exercício: 1137. N-th Tribonacci Number
**Objetivo**: Dada uma inteiro $n$ indique qual é o n-ésimo termo da Sequência de "Tribonacci" (sequência de Fibonacci em que a soma é dos 3 elementos anteriores, e não dos 2);

## Descrição geral da estratégia
Para resolver gero a Sequência de "Tribonacci" de maneira iterativa com memoization. Nesse contexto, salvo os resultados parciais em um array, retornando o último elemento do array.

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$