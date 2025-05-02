## Exercício: 268. Missing Number
**Objetivo**: Dada uma lista de inteiros consecutivos (desordenados) determinar qual elemento está faltando na lista (e.g. lista com 99 número de 0 à 100, aí vai estar faltando algum elemento na lista);

## Descrição geral da estratégia
Criei duas variáveis: `expected` e `real`. Na primeira eu armazeno a soma esperada para a lista, enquanto na segunda guardo qual é a soma real. Por fim, apenas retorno a diferença entre essas duas variáveis.

## Análise de complexidade
Para uma lista com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(1)$, ($\Theta(2)$)

## Obs:
O jeito mais apropriado seria com divisões inteiras por $10$ e por $10^(n - i)$, mas fiquei com preguiça de ajeitar isso porque queria ir para o churrasco.