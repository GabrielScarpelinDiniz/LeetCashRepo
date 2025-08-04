## Exercício: 55. Jump Game
**Objetivo**: Dado um array de inteiros que representa quanto se pode pular ([1, 2, 3, 4] indica que, a partir da casa 0, pode-se pular para a casa 1, da casa 1 pode-se pular para a casa 2 e 3 e assim por diante) determine se é possível chegar ao final do array.

## Descrição geral da estratégia
Para resolver uso uma abordagem de programação dinâmica que vai progressivamente salvando se é possível chegar a determinada casa. Para isso, crio um array de booleanos `canBeReached` com todos os elementos falsos, exceto o primeiro (só é possível chegar no primeira casa no início). A partir desse array, vou mudando para verdadeiro cada elemento que é possível alcançar a partir de um elemento `i`. Se não for possível chegar em uma determinada casa, retorna-se `false`. Caso se chegue ao final do array, retorna-se `true`. Caso as condicionais anteriores não sejam atendidas, retorna-se o valor presente no último elemento do array `canBeReached`.

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n^2)$ 
- **Space complexity**: $O(n)$
