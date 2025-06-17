## Perímetro da Ilha (Island Perimeter)

O método `IslandPerimeter` calcula o perímetro de uma ilha representada em uma grade 2D, onde `1` indica terra e `0` indica água. A grade é completamente cercada por água e contém exatamente uma ilha.

**Funcionamento:**

1. Percorre cada célula da grade.
2. Para cada célula de terra (`1`), verifica os quatro lados:
   - Se estiver na borda da grade ou adjacente a uma célula de água (`0`), incrementa o perímetro.
3. Soma as contribuições de todas as células de terra.

**Exemplos:**

- Entrada: `[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]`

  - Saída: `16`
  - Explicação: Cada lado exposto ao exterior ou à água contribui para o perímetro.

- Entrada: `[[1]]` → `4`
- Entrada: `[[1,0]]` → `4`

**Complexidade de Tempo:** O(m × n), onde m e n são as dimensões da grade.

**Complexidade de Espaço:** O(1), pois utiliza apenas variáveis simples.
