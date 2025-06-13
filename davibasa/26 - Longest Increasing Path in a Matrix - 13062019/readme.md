## Caminho Crescente Mais Longo em uma Matriz (Longest Increasing Path in a Matrix)

O método `LongestIncreasingPath` encontra o comprimento do caminho crescente mais longo em uma matriz de inteiros. A partir de cada célula, é possível mover-se em quatro direções: esquerda, direita, cima ou baixo.

**Funcionamento:**
1. Utiliza DFS (Depth-First Search) com memoização para explorar todos os caminhos possíveis.
2. Para cada célula da matriz, calcula o caminho crescente mais longo que começa nessa célula.
3. A memoização evita recálculos, armazenando o resultado de cada célula já processada.
4. Explora as 4 direções adjacentes apenas se o valor da célula vizinha for maior que o atual.

**Exemplos:**
- Entrada: [[9,9,4],[6,6,8],[2,1,1]]
- Saída: 4
- Explicação: O caminho mais longo é [1, 2, 6, 9].

- Entrada: [[3,4,5],[3,2,6],[2,2,1]]
- Saída: 4
- Explicação: O caminho mais longo é [3, 4, 5, 6].

**Complexidade de Tempo:** O(m × n), onde m e n são as dimensões da matriz. Cada célula é visitada no máximo uma vez devido à memoização.

**Complexidade de Espaço:** O(m × n), para a matriz de memoização e a pilha de recursão.
