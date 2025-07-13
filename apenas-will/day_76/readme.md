## Exercício: 347. Top K Frequent Elements
**Objetivo**: Dado array de inteiros e um inteiro k, retorne uma lista contendo os k elementos que mais se repetem no array.

## Descrição geral da estratégia
Para resolver crio um `HashMap` que tem como chave um inteiro e como valor a quantidade de vezes que esse elemento aparece no array. Em seguida, coloquei os elementos do `HasMap` em uma fila de prioridade, usando como parâmetro para a prioridade a contagem desses elementos. Ao final, removi, um a um, os elementos dessa fila, adicionando-os no array de saída, retornando-o ao final.

## Análise de complexidade
Para uma array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$ 