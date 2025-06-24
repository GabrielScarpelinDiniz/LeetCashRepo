## Exercício: 21. Merge Two Sorted Lists
**Objetivo**: Dada duas listas ligadas ordenadas, combine as duas, gerando uma única lista ligada ordenada;

## Descrição geral da estratégia
Para resolver, crio uma marcador para o início da lista de resultado e três ponteiros auxiliares, um para a primeira lista, um para a segunda lista e um para a lista de resultado. Em seguida, comparo os nós em cada dos ponteiros, adicionando o menor deles como seguinte ao ponteiro da lista de resultado. Ao final, retorno o nó seguinte ao nó de referência criado inicialmente.

## Análise de complexidade
Para um duas listas com, respectivamente, $n$ e $m$ nós, tem-se:
- **Time complexity**: $O(n + m)$
- **Space complexity**: $O(1)$