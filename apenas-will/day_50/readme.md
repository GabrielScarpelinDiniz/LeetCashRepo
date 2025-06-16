## Exercício: 384. Shuffle an Array
**Objetivo**: Dada uma array de inteiros `nums`, gere um algoritmo capaz de embaralhar o array;

## Descrição geral da estratégia
Para resolver implementei uma função que embaralha o array usando o algoritmo de Fisher–Yates. Esse algoritmo funciona iterando por cada elemento do array de trás para frente, trocando-o com algum outro elemento (com índice menor do que o que será trocado) aleatório do array.

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$ (a implementação deve ser feita com uma classe, obrigando a utilização de arrays auxiliares) 