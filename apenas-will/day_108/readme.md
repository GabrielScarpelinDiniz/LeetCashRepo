## Exercício: 326. Power of Three
**Objetivo**: Dado um inteiro n, determine se n é uma potência de 3 ( $\exists x \, (n = 3^x)$ ).

## Descrição geral da estratégia
Para resolver implemento o comportamento padrão da fatoração. Basicamente, de forma recursiva, confiro se um elemento é igual à 0, retornando `false`, se é igual à 3 ou 1, retornando `true`. Se ele for divisível por 3, retorno o valor da própria função com o valor dividido por 3. Caso nenhuma das condições anteriores seja atingida, retorno `false`.

## Análise de complexidade
Para um inteiro $n$, tem-se:
- **Time complexity**: $O(\log(n))$ 
- **Space complexity**: $O(\log(n))$
