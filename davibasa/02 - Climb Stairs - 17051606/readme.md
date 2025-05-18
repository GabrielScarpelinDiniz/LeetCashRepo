## Climb Stairs

Calcula o número de maneiras distintas de subir uma escada com `n` degraus, onde você pode dar 1 ou 2 passos de cada vez. Utiliza uma abordagem de recursão com memoização (uma técnica de programação dinâmica) para encontrar a solução. Um dicionário (`memo`) é usado para armazenar os resultados de subproblemas já calculados (ou seja, o número de maneiras de subir `k` degraus). Quando a função é chamada para um número de degraus `k` cujo resultado já foi calculado e armazenado no dicionário, esse valor é retornado diretamente, evitando recálculos redundantes que levariam a uma complexidade exponencial em uma abordagem puramente recursiva.

**Complexidade de Tempo:** O(n), onde `n` é o número total de degraus.

**Complexidade de Espaço:** O(n).
O espaço é utilizado principalmente por duas fontes:

1.  O dicionário `memo`: No pior caso, ele armazenará os resultados para `n` chaves distintas (de `n` até 2, pois 0 e 1 são casos base que não resultam em armazenamento explícito no `memo` antes de retornar).
2.  A pilha de chamadas da recursão: A profundidade máxima da pilha de recursão será `n`, pois uma chamada para `ClimbStairsRecursive(n)` pode levar a uma cadeia de chamadas como `ClimbStairsRecursive(n-1)`, `ClimbStairsRecursive(n-2)`, ..., até `ClimbStairsRecursive(0)`.
    Ambos os fatores contribuem para uma complexidade de espaço linear.
