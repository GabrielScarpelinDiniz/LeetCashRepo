## Exercício: 658. Find K Closest Elements
**Objetivo**: Dada uma lista ordenada de inteiros, um valor $k$ e um valor target $x$, determine o $k$ elementos mais próximos de $x$. Um elemento $a$ é mais próximo de $x$ do que $b$ se:

```math
|a-x| < |b-x| \lor (|a-x| = |b-x| \land a<b)
```

## Descrição geral da estratégia
Para resolver, implemento uma função de avaliação `eval` que determina qual de dois valores `a` e `b` são mais próximos de `x` (retorna 1 se $a$ é mais distante que $b$ e -1 caso contrário. Essa função é o inverso do padrão para facilitar na etapa a seguir). Em seguida, crio uma lista de prioridade que organiza em uma max-heap os elementos por ordem de distância (quanto mais próximo de $x$, mais perto do final estará o elemento), adicionando elementos até a quantidade $k$ e removendo-os caso esse tamanho seja ultrapassado. Ao final, coloco todos os elementos da fila de prioridade em uma lista, ordeno a lista e a retorno (os valores devem estar em ordem crescente).

## Análise de complexidade
Para um array com $n$ inteiros e um valor $k$, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(k)$
