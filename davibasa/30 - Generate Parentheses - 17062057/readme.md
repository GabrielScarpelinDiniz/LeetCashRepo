## Gerar Parênteses (Generate Parentheses)

O método `GenerateParenthesis` gera todas as combinações possíveis de n pares de parênteses bem formados.

**Definição:**
Uma combinação de parênteses é considerada "bem formada" se para cada parêntese de abertura há um parêntese de fechamento correspondente, e todos os parênteses são fechados na ordem correta.

**Funcionamento:**
1. Utiliza backtracking para construir combinações válidas.
2. Mantém controle da quantidade de parênteses de abertura e fechamento já usados.
3. Adiciona parêntese de abertura '(' se ainda não usou todos (open < n).
4. Adiciona parêntese de fechamento ')' apenas se houver parênteses de abertura não fechados (close < open).
5. Quando a string atual tem comprimento 2*n, adiciona à lista de resultados.

**Exemplos:**
- Entrada: n = 3 → ["((()))","(()())","(())()","()(())","()()()"]
- Entrada: n = 1 → ["()"]

**Complexidade de Tempo:** O((4^n)/√n), usando a aproximação do n-ésimo número de Catalan.

**Complexidade de Espaço:** O(n), para a profundidade da recursão e o armazenamento das combinações.
