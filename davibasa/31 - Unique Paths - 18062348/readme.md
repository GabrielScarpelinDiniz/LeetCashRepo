## Caminhos Únicos (Unique Paths)

O método `UniquePaths` calcula o número de caminhos únicos que um robô pode fazer em uma grade m x n, movendo-se apenas para a direita ou para baixo, do canto superior esquerdo ao canto inferior direito.

**Funcionamento:**
1. Utiliza programação dinâmica para preencher uma matriz `dp` onde `dp[i, j]` representa o número de caminhos até a célula (i, j).
2. Inicializa a primeira linha e a primeira coluna com 1, pois só há um caminho para cada célula dessas bordas.
3. Para cada célula restante, soma os caminhos vindos de cima e da esquerda.
4. O resultado final está em `dp[m-1, n-1]`.

**Exemplos:**
- Entrada: m = 3, n = 7 → Saída: 28
- Entrada: m = 3, n = 2 → Saída: 3

**Complexidade de Tempo:** O(m × n)

**Complexidade de Espaço:** O(m × n), para a matriz de DP.
