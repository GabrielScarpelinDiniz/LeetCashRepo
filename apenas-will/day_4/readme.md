## Exercício: 9. Palindrome Number
**Objetivo**: Dado um inteiro x, determine se ele é um palíndromo (x é igual a x de trás para frente);

## Descrição geral da estratégia
Converti o número para uma string e posicionei um "ponteiro" no incio e fim dele. Caso o valor dos ponteiros fosse diferente, retornava `false`.

## Análise de complexidade
Para um número de $n$ algarismos, tem-se:
- **Time complexity**: $O(n)$ ($\Theta(n/2)$)
- **Space complexity**: $O(n)$

## Obs:
O jeito mais apropriado seria com divisões inteiras por $10$ e por $10^(n - i)$, mas fiquei com preguiça de ajeitar isso porque queria ir para o churrasco.