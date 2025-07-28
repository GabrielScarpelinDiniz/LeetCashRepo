## Exercício: 2044. Count Number of Maximum Bitwise-OR Subsets
**Objetivo**: Dado um array de inteiros, retorne quantos subconjuntos tem valor igual ao maior _Bitwise-OR_ (OR bit a bit do inteiro) do array.

## Descrição geral da estratégia
Para resolver utilizo de um backtracking que incrementa o valor de uma variável auxiliar todas as vezes que encontra um subconjunto válido. Primeiramente, determino qual é o maior _Bitwise-OR_ do array (que para arrays sem números negativos, como neste caso, é o _Bitwise-OR_ de todos os elementos do array). Em seguida, implemento um método de backtracking que explora os subconjuntos obtidos com os elementos do array original, calculando seu _Bitwise-OR_. Caso o valor obtido seja menor que o máximo, esse valor é explorado ara averiguar se a partir dessa escolha pode-se atingir o máximo previamente determinado. Caso o valor seja igual ao máximo, uma variável auxiliar é incrementada, indicando que mais um subconjunto válido foi encontrado. O processo continua até que todas as possibilidades tenham sido exploradas. Por fim, o valor da variável auxiliar é retornado.

## Análise de complexidade
Para um array com $n$ elementos, tem-se:
- **Time complexity**: $O(2^n)$ 
- **Space complexity**: $O(n)$
