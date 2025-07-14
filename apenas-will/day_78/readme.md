## Exercício: 215. Kth Largest Element in an Array
**Objetivo**: Dado uma array de inteiros e um inteiro $k$, determine o k-ésimo maior elemento do array.

## Descrição geral da estratégia
Para resolver usei primeiro defino uma lista de prioridade que armazenará os menores elementos do meu array em ordem. Em seguida, itero pelo array colocando os elementos na lista de prioridade até que ela atinja uma quantidade $k$ de elementos. Caso isso ocorra, eu removo o elemento do topo da fila, mantendo até $k$ elementos. Ao final, visto que o primeiro elemento da fila de prioridade é o menor e que lá há $k$ elementos, então esse menor é o elemento de interesse, sendo retornado ao final do loop; 

## Análise de complexidade
Para um array com $n$ elementos e um inteiro $k$, tem-se:
- **Time complexity**: $O(n \log(k))$
- **Space complexity**: $O(k)$ 