## Exercício: 784. Letter Case Permutation
**Objetivo**: Dado uma string s, retorne todas as strings que podem ser formadas mudando os caracteres para maiúsculo ou minúsculo.

## Descrição geral da estratégia
Para resolver usei uma abordagem de backtracking que itera por cada caracter da string conferindo se ele é uma letra. Caso seja, a função é chamada recursivamente para explorar um caso em que esse caracter é maiúsculo e, em seguida, um que ele é minúsculo. Quando se chega ao final da string, salvo o resultado em na lista `res`, que é retornada ao final.

## Análise de complexidade
Para uma string com $n$ caracteres, tem-se:
- **Time complexity**: $O(2^n)$
- **Space complexity**: $O(2^n)$ 