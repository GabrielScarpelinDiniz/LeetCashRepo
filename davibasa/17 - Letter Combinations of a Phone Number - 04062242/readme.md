## Combinações de Letras de um Número de Telefone (Letter Combinations of a Phone Number)

O método `LetterCombinations` gera todas as combinações possíveis de letras que um número de telefone pode representar, com base no mapeamento de dígitos para letras.

**Exemplo:**

- Entrada: "23"
- Saída: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

**Funcionamento:**

1. Se a entrada estiver vazia, retorna uma lista vazia.
2. Utiliza um mapeamento de dígitos para letras, como em teclados de telefone.
3. Usa backtracking para gerar todas as combinações possíveis.

**Complexidade de Tempo:** O(4^n), onde n é o comprimento da string de entrada.

**Complexidade de Espaço:** O(n), para armazenar a combinação atual durante o backtracking.
