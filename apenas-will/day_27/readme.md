## Exercício: 485. Max Consecutive Ones
**Objetivo**: Dada um array de binários, indique qual é a maior sequência de "1" consecutivos;

## Descrição geral da estratégia
Para resolver, usei dois ponteiros, um posicionado antes do inicio do array e um na primeira posição. A cada iteração de um loop, o segundo ponteiro andava para frente, enquanto o segundo permanecia na sua posição. Caso o segundo ponteiro se deparasse com um "0", então o valor da variável `max` era atualizado com a diferença entre a posição de ambos os ponteiros. O ponteiro de trás era atualizado para a posição atual do ponteiro da frente e o ciclo se repete até o final do array.

## Análise de complexidade
Para um array com $n$ bits, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$ 