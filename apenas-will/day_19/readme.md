## Exercício: 141. Linked List Cycle
**Objetivo**: Dada um node que é a head de uma lista ligada, determine se essa lista possui um ciclo ou não (um ciclo ocorre quando um nó referencia um nó previo da lista, de modo que a lista fica sem final);

## Descrição geral da estratégia
Para resolver, inicializei dois ponteiros no inicio da lista, um rápido e um lento. O rápido anda com o dobro da velocidade do lento e, por isso, se houver um ciclo, eventualmente, eles vão colidir. Se houver uma colisão, significa que a lista possui um ciclo, caso contrário, se o ponteiro rápido chegar ao final da lista, significa que a lista não tem ciclos. (curiosidade: o nome desse algoritmo é algoritmo de Floyd)

## Análise de complexidade
Para uma lista com $n$ nodes, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$