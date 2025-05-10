## Exercício: 58. Length of Last Word
**Objetivo**: Dada uma string que contém uma frase, determine o comprimento da última palavra dessa frase;

## Descrição geral da estratégia
Para resolver apenas iterei na string de trás para frente, e, caso eu encontrasse um caracter diferente de " ", eu acrescia em 1 o valor de uma variável que guardava o tamanho da palavra.

## Análise de complexidade
Para uma string com $n$ caracteres, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$