## Sudoku Válido (Valid Sudoku)

O método `IsValidSudoku` verifica se um tabuleiro de Sudoku 9x9 parcialmente preenchido é válido segundo as seguintes regras:

1. Cada linha deve conter os dígitos de 1 a 9 sem repetição.
2. Cada coluna deve conter os dígitos de 1 a 9 sem repetição.
3. Cada um dos nove blocos 3x3 da grade deve conter os dígitos de 1 a 9 sem repetição.

**Nota:** Apenas as células preenchidas precisam ser validadas. Um tabuleiro de Sudoku válido não é necessariamente solúvel.

**Funcionamento:**

1. Utiliza conjuntos (HashSet) para rastrear dígitos em cada linha, coluna e bloco 3x3.
2. Percorre cada célula do tabuleiro, verificando se o valor já existe nos conjuntos correspondentes.
3. Se encontrar uma duplicata em qualquer linha, coluna ou bloco, retorna false.

**Complexidade de Tempo:** O(1), pois o tamanho do tabuleiro é fixo em 9x9.

**Complexidade de Espaço:** O(1), pois utiliza uma quantidade fixa de espaço para os conjuntos.
