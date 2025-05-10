## Exercício: 67. Add Binary
**Objetivo**: Dadas duas strings que representam dois números inteiros em binário, retorne uma string que é a soma dos dois inteiros;

## Descrição geral da estratégia
Para resolver apenas apliquei o algoritmo padrão de soma para números na base 2, realizando as somas dos bits individuais e salvando se era necessário somar 1 à próxima soma ou não.

## Análise de complexidade
Para uma string com $n$ bits, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$