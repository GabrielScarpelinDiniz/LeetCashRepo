## Minimum Cost to Move Chips to The Same Position

O método `MinCostToMoveChips` calcula o custo mínimo para mover todas as fichas para a mesma posição.

**Funcionamento:**

- Movimentos de 2 em 2 não têm custo, então todas as fichas podem ser movidas livremente entre posições pares ou entre posições ímpares.
- O custo só ocorre ao mover fichas de uma paridade para outra (par para ímpar ou ímpar para par).
- Basta contar quantas fichas estão em posições pares e quantas em ímpares. O custo mínimo é o menor desses dois valores.

**Exemplos:**

- Entrada: [1,2,3] → Saída: 1
- Entrada: [2,2,2,3,3] → Saída: 2
- Entrada: [1,1000000000] → Saída: 1

**Complexidade de Tempo:** O(n), onde n é o número de fichas.

**Complexidade de Espaço:** O(1), pois só utiliza variáveis simples.
