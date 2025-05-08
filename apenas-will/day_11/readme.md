## Exercício: 121. Best Time to Buy and Sell Stock
**Objetivo**: Dado um array de inteiros que representam preços de ações ao longo do tempo, determine qual é o lucro máximo que pode ser obtido comprando uma ação e vendendo-a no futuro;

## Descrição geral da estratégia
Para resolver, coloquei dois ponteiros no início do array. O ponteiro `fa` representa um ponteiro rápido, o qual anda a cada iteração de um loop, enquanto o `sl` representa um ponteiro lento, que só tem seu valor alterado caso a diferença entre os elementos da posição `fa` e `sl` seja maior que o máximo encontrado anteriormente ou se o valor presente na posição `fa` seja menor que o da posição `sl`. Assim, o algoritmo sempre busca a maior diferença, fazendo isso seguindo o padrão que sempre o valor de `fa` tem que ser maior que o de `sl`. 

## Análise de complexidade
Para um array com $n$ elementos, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$
