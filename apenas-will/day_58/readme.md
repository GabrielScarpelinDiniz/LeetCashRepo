## Exercício: 167. Two Sum II - Input Array Is Sorted
**Objetivo**: Dada um array de inteiros ordenado, indique o índice de dois elementos que, somados, resultam em um `target`;

## Descrição geral da estratégia
Para resolver, adiciono dois ponteiros ao array, um no início e outro no final. Após isso, enquanto os dois forem diferentes, calculo a soma dos elementos nesses índices. Se a soma resultar no `target`, retorno. Caso contrário, verifico se ela é maior que o `target`, decrementando o ponteiro mais próximo ao final do array em 1 posição, incrementando, por fim, o ponteiro mais próximo ao início caso a soma seja menor que o `target`.

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$