## Exercício: 20. Valid Parentheses
**Objetivo**: Dada uma string que contém "parênteses" `()`, `[]` e `{}`, veja se tudo que foi aberto se fechou;

## Descrição geral da estratégia
Para resolver criei uma stack em que, quando era um caracter de abertura, adicionava o elemento na stack e, quando era um de fechamento, eu o removia da stack. Sobre edge cases, adicionei um `if` inicial para strings vazias e de um elemento, e adicionei uma verificação caso um caracter de fechamento fosse adicionado no inicio da string.

## Análise de complexidade
Para uma string com $n$ caracteres, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$