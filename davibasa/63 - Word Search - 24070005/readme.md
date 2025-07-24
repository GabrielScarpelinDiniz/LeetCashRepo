## Word Search

O método `Exist` verifica se uma palavra pode ser formada percorrendo células adjacentes em um grid de caracteres.

### Funcionamento:

1. **Busca inicial**: Tenta iniciar a busca a partir de cada célula do grid.
2. **DFS com backtracking**: Usa busca em profundidade para explorar caminhos possíveis.
3. **Marcação de visitados**: Marca células como visitadas temporariamente para evitar reutilização.
4. **Exploração de direções**: Verifica as 4 direções (cima, baixo, esquerda, direita).
5. **Backtracking**: Restaura o estado original da célula após exploração.

### Exemplos:

- Entrada: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"`
  Saída: `true`
- Entrada: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"`
  Saída: `true`
- Entrada: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"`
  Saída: `false`

### Complexidade:

- **Tempo:** O(m × n × 4^L), onde m×n é o tamanho do grid e L é o comprimento da palavra.
- **Espaço:** O(L) para a pilha de recursão.

### Otimizações:

- Poda precoce quando caractere não coincide
- Backtracking eficiente modificando o grid in-place
- Verificação de limites antes da recursão
