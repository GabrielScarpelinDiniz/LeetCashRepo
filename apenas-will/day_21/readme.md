## Exercício: 412. Fizz Buzz
**Objetivo**: Dada um inteiro $n$, retorne um array contendo todos os inteiros até $n$, porém, caso um inteiro seja divisível por 3 retorne "Fizz", caso ele seja divisível por 4 retorne "Buzz" e caso ele seja divisível por ambos, retorne "FizzBuzz";

## Descrição geral da estratégia
Para resolver, implementei o comportamento descrito anteriormente, usando um loop e condicionais.

## Análise de complexidade
Para uma inteiro $n$, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$ (para gerar o output, $O(1)$ espaço auxiliar)