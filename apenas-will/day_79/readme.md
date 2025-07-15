## Exercício: 414. Third Maximum Number
**Objetivo**: Dado uma array de inteiros e um inteiro, retorne o terceiro maior elemento distinto do array. Se o array não tiver pelo menos 3 elementos distintos, retorne o maior.

## Descrição geral da estratégia
Para resolver usei primeiro defino uma lista de prioridade que armazenará os menores elementos do array em ordem. Em seguida, itero pelo array conferindo se ele é único ou se está duplicados, se for único, coloco-o na lista de prioridade até que ela atinja uma quantidade de 3 de elementos, ignorando-o caso contrário. Caso a lista alcance mais de 3 elementos, removo o elemento do topo da fila, mantendo até 3 elementos. Após o loop principal, confiro se a lista possui pelo menos 3 elementos e, se não tiver, itero pela lista de prioridade retornando o maior elemento. Por fim, visto que o primeiro elemento da fila de prioridade é o menor e que lá há 3 elementos, então esse menor é o elemento de interesse, sendo retornado ao final do loop;  

## Análise de complexidade
Para um array com $n$ elementos, tem-se:
- **Time complexity**: $O(n)$ ( $\Theta(n \log(3))$ )
- **Space complexity**: $O(1)$ 