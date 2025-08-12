## Exercício: 118. Pascal's Triangle
**Objetivo**: Dada um número inteiro entre 1 e 30, retorne uma lista contendo as listas de elementos de cada linha do Triângulo de Pascal até o valor do inteiro.

## Descrição geral da estratégia
Para resolver, implemento o comportamento do Triângulo de Pascal de maneira iterativa. Primeiro, caso esteja adicionando o primeira linha do triângulo, adiciono uma lista com o elemento 1. Em seguida, de maneira iterativa, construo a linha do Triângulo, no qual um elemento `i` da linha atual é igual a soma dos elementos `i` e `i - 1` da linha anterior. Repito o processo até gerar a linha inteira, adicionando-a à lista de listas de `res`, que é retornada no final.  

## Análise de complexidade
Para um inteiro $n$, tem-se:
- **Time complexity**: $O(n^2)$ 
- **Space complexity**: $O(n^2)$
