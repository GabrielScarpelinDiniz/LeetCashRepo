## Exercício: 83. Remove Duplicates from Sorted List
**Objetivo**: Dada uma lista ligada ordenada, remova elementos duplicados;

## Descrição geral da estratégia
Para resolver, iterei pela lista ligada com dois ponteiros, `sl` e `fa`. A cada iteração, `fa` move 1 nó para frente, enquanto `sl` só se move quando o valor dele e de `fa` são diferentes. Com isso, quando a condição de mudança de `sl` é atingida, o elemento seguinte a `sl` é definido como `fa` e ambos vão para a mesma posição seguinte à `fa`. Essa técnica é popularmente conhecida como _reset/catch-up two pointers technique_

## Análise de complexidade
Para uma lista com $n$ nós, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$ 